## Bypass .htaccess

If we can upload a file to a web server with an interpreted language, e.g. PHP, then we just need to be able to drop the file in a folder that is served and processed.

If a `.htaccess` or similar file prevents these files from executing, we can try to:

* Override/change the `.htaccess` or equivalent file
* Use `../` tricks to change where our file is uploaded to
* Find a way to change global configurations of the web server that dictate the default folder where files are uploaded to
* If zip files are accepted and uncompressed, use relative paths in the zip file to write files outside of the unzip location

## Bypass file type filters to obtain execution

Apache (and other) can typically handle extensions other than the language in use (.e.g PHP).  Developers may block the expected extensions, but we may be able to bypass by choosing another script format instead.  It is unlikely that developers were successful in blacklisting all potential executable formats:

* .exe
* .asp
* .aspx
* .php
* .php3
* ,phtml
* .bat
* .cgi
* .pl
* .com
* .vbs
* .reg
* .pcd
* .pif
* .scr
* .bas
* .inf
* .vb
* .vbe
* .wsc
* .wsf
* .wsh

## Loose and strict type comparisons.  

## String to integer conversion rules.

Older versions of PHP use loose type comparisions and _will evaluate comparisons with two strings as if they were numbers_, when both strings are valid representations of a number (e.g. decimal, hexadecimal, exponential)!  

The same holds true when one argument is a string and the other a number. 

```php
var_dump('0xAAAA' == '4390')
bool(true)
var_dump('0xAAAA' == 4390)
bool(true)
```

For exponential numbers (a.k.a. scientific notation) this still works on both old and new PHP versions.

```php
var_dump('0e1111' == '0')
>> bool(true)
var_dump('0e1111' == 0)
>> bool(true)
```

In interesting note for the ATutor vulnerability here, is that even though it takes and MD5 hash (that we partically control) and another string (that we control), we can bypass this because the MD5 hash of 240610708 happens to look like an exponential number!

```php
echo md5('240610708')
>> 0e462097431906509019562988736854
var_dump(md5('240610708') == '0')
>> bool(true)
```

## PHP

Dump some server information if we can find a way to upload files:

```php
<?php phpinfo(); ?>
<?php phpversion(); ?>
<?php var_dump(get_magic_quotes_gpc()); ?>
```

## Java

Often has `.do` extensions for compiled Java app web routes.  The are mapped to functions in the code that start with the name `do` followed by the HTTP Method name, e.g. `void doGet(HttpServletRequest, HttpServletResponse)` and `void doPost(...)`.  The `HttpServletRequest.getParameter()` method implies user controlled input.

The `WEB-INF/` folder usually holds the app configuration. `WEB-INF/web.xml` holds web app route mappings for servlets and the location of the `.jar` files implementimg them.