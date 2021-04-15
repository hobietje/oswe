[Code Audits 1 - Fall 2011](https://vimeo.com/30001189)
[Code Audits 2 - Fall 2011](https://vimeo.com/29702192)

# Process

Understand what the app does!

Find areas to target:
* Typical areas:
  * Data input sources and output targets
  * Security mechanisms, e.g. authN/Z
  * Complex parsing, protocols, data management
* Comments - particularly indicating ommissions or complexity:
  * FIXME
  * TODO
  * XXX
  * Swearing
  * Typos
* Code that is likely:
  * Old code - not up to date with security practices
  * Imported/copied code - not sanity checked
  * Rushed code - not adequately reviewed bugfixes, deadlines, ...
  * Code by a developer known to write poor code
  * Repeated patterns from other vulnerabilities discovered

Using grep:
* Great for:
  * Find sensitive API usage
  * Finding where in the code auth/etc are done
* Beware: 
  * easy to have lots of 'potential' vulnerabilties
  * hard to trace usage
  * hard to confirm they are in useful areas of the app
  * doesn't show logic flaws

__LEARN TO SKIP UNIMPORTANT CODE!__ You can always come back later.

Implementations bugs:
* Failure to validate input, e.g. trusting input or assuming structure
* Misure or misunderstanding of an API or abstraction, e.g. forgot to call X
* Miscalculation of an operation, e.g. off-by-one errors
* Failure to verify the results of an operation, e.g. assume success
* Application state failures, e.g. skip/bypass steps
* Failure to track relationships, e.g. object references

# Examples

## Memory Corruption Bugs

Typically using `strcpy()`, `strcat()`, `sprintf()`, `gets()`, etc and homegrown equivalents.

```c++
int vulnerable(char *userstring) {
    char buf[128];
    strcpy(buf, userstring);
    return;
}
```

Can still be found with length limited equivalents like `strncpy()` or `strncat()` that try to prevent this bug class, because they still assume the dev will pass in a _correct_ length.  Common mistakes include:
* using the length of the input rather than target buffer
* allowing an attacker to control the length directly
* miscalculating the length, esp. given the need for C strings to have a `\0` byte at the end
* miscalculations due to failing to account for multi-byte characters, e.g. `wchar` type, and misusing related APIs like `mbstowcs()`. I.e. count of characters vs their size in bytes.
* failing to account for already existing data in a buffer
* copy-pasting code relating to buffers, then failing to adjust the buffer lengths or # of bytes to copy

_Find string copy and manipulation functions and review the arithmetic used for string size calculations and copying is correct!_

## Data Type Bugs

Incorrect use of signed vs unsigned types, resulting in:
* Integer overflows
* Pointers, which are unsigned ints and can overflow too
* (also, example below fails to check that `malloc` was succesful and didn't return `NULL`)

```c++
int getData(int socket) {
  unsigned int len;
  char *buf = NULL;
  len = getDataLen(socket);
  buf = malloc(len + 1);
  read(socket, buf, len);
  buf[len + 1] = 0x0;
}
```

Can often be hard to detect due to implicit conversions from signed to unsigned types by the language, e.g. when calling a function.

_Find them by searching for `malloc` and other memory functions and check the arithmetic and bounds checks of dynamic memory allocations._

_Still exists in Java/.NET, but will lead to logic flaws rather than memory corruption._

Types of different length, e.g. char/short/int/long, may also be used and mixed in the same context and their values truncated as a result.

_Look for the types used in size calculations and bounds checks.  Are types appropriately signed/unsigned?  Are data type sizes mixed?  Are variables being added that may result in an overflow after addition?_

## Metacharacter Injection

Quotes, semi-colons, non-printable, NUL terminator, etc.

```c++
void extractUserZip(char *userFile) {
  char command[1024];
  snprintf(command, 1023, "unzip %s", userfile);
  system(command);
  return;
}
```

Various kinds of injections:
* Command injection, e.g. `;` in `unzip x.zip; echo /etc/passwd`
* SQL injection, i.e. terminate a string, start a comment, etc
* Embedded delimeters, e.g. `user:pass\nnewuser:newpass`
* NUL injection, e.g. terminate filenames like `bob\0.txt`
* Trunaction, e.g. file path being shortened due to buffer size, thus allowing attacker to spoof extension like `toolong.php.txt`


"The Art of Software Security Assessment: Identifying and Preventing Software Vulnerabilities" chapter on "Metacharacters" has a wide list of use cases and examples, including:

* Path metacharacters:
  * Directory traversals with `/` and `\`, including how they are handled in multi-OS code
  * File Canonicalization:
    ```
    C:\WINDOWS\system32\drivers\..\calc.exe
    calc.exe
    .\calc.exe
    ..\calc.exe
    \\?\WINDOWS\system32\calc.exe
    ```
  * Windows Registry paths can be susceptable to truncation as  `\\SOFTWARE\\MyProduct` is equivalent to `\\SOFTWARE\\\\\\\\MyProduct`
* C format strings, i.e. calls to `printf()`, `err()` , `syslog()`, etc that use untrusted input as part or all of the format string
* Shell metacharacters, i.e. calls to `execve()`, `CreateProcess()`, `system()`, `popen()`, etc that accept any of:
  * `;` (separator)
  * `|` (pipe)
  * `&` (background)
  * `<` (redirect)
  * `>` (redirect)
  * ``` ` ``` (evaluate)
  * `!` (not operator)
  * `-` (argument switch)
  * `*` (wildcard)
  * `/` (slash)
  * `?` (question)
  * `(` (open parenthesis)
  * `)` (close parenthesis)
  * `.` (wildcard)
  * `;` (separator)
  * ` ` (space)
  * `[` (open bracket)
  * `]` (close bracket)
  * `\t` (tab)
  * `^` (caret)
  * `~` (homedir)
  * `\` (escape)
  * `\\` (backslash)
  * `'` (quote)
  * `"` (double quote)
  * `\r` (carriage return)
  * `\n` (newline)
  * `$` (variable)
* Perl `popen()` can be called with three arguments (file handle,
mode, and filename) or two arguments (file handle and filename). The second
method determines in which mode to open the file by interpreting metacharacters
that might be at the beginning (usually) or end of the filename and can be used to inject commands:
  * `<` Open file for read access (default behaviour).
  * `>` Open file for write access; create file if it doesn't exist.
  * `+<` Open file for read-write access.
  * `+>` Open file for read-write access; create file if it doesn't exist; otherwise, truncate the file.
  * `>>` Open file for write access but don't truncate; append to the end of the file.
  * `+>>` Open file for read-write access but don't truncate; append
to the end of the file.
  * `|` This argument is a command, not a filename. Create a pipe to run this command with write access.
  * `|` (at end) This argument is a command, not a filename. Create a pipe to run this command with read access.
* SQL query injections and SQL truncation
* ...

Consider the layering/nesting of technologies, e.g. PHP is not vulnerable to NUL injection itself (maintains string lengths) but uses a lot of C libraries under the hood (which DOES observe NUL bytes):
 
```php
fopen(../../etc/passwd\0.txt)
```

_Look for anything executing commands, accessing files, running queries, etc that uses user controllable input._