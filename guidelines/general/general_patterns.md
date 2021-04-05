# Code Comments

Check for code comments that say something isn't implemented or working as intended.  E.g. anything mentioning:
* todo
* temporarily
* disabled
* skip
* hack

# Incorrect Use

Look for functions that were built with security in mind, but aren't called correctly.  E.g.

```
func querydb(sql, params) { ... }
querydb('SELECT * FROM users WHERE User=' + userId, {})
```

# Missing braces

```
if (i != 0)
    foo(i);
    bar(i);
```

The body of the `if` statement is not enclosed in braces.  The second line of code may (as indicated by the indenting) or may not (as indicated by the lack of brackets) be intended to be inside that `if` condition.

# To encode or not to encode [[ref](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/)]

Given pseudocode in a backend writing HTML code:

```
Write "Hello, " & Request("name")
```

Your site is already vulnerable to XSS attacks. You have to encode the user input before you copy it back into the HTML.

```
s = Encode(Request("name"))
```

You would think one solution is to encode all strings right away,  All strings that originate from the user are unsafe after all. Any unsafe string must not be output without encoding it.

Unfortunately, you want to store these user strings in a database somewhere, and it doesn’t make sense to have them stored HTML-encoded in the database.

```
s = Request("name")
Write Encode(s)
```

This solution also doesn't work.  Whenever you see a naked `Write` without the `Encode` you would think something is amiss, but sometimes you have little bits of HTML around in your code and you can’t encode them.  For example:

```
If mode = "linebreak" Then prefix = "<br>"

Write prefix
```

One proposal is to prefix variable and function names with an `unsafe`/`us` or `safe`/`s` prefix.  That allows us to know whether the value has been escaped or not.  This is a lot better.

```
sName = Encode(Request("name"))
Write "<script>" + sName + "</script>"
```

Unfortunately, it is still not perfect as it doesn't consider different types of encoding.  You should be JavaScript-encoding the `sName` here rather than HTML-encoding it.

# Mime Types

Code may not handle mime types correctly or consistently. 

* Try sending requests using different mime types.  
* Try requesting responses using different mime types.

# SQL Injection

Sample vulnerabilities:

* [ImpressCMS: SQL injection when configuring a database](https://hackerone.com/reports/983710)

# LFI

Sample vulnerabilities:

* [ImpressCMS: Fixed possible file system exposing due language cookie](https://github.com/ImpressCMS/impresscms/pull/821/files)

# DoS

Sample vulnerabilities:

* [ImpressCMS: Limit maximum length of password](https://github.com/ImpressCMS/impresscms/pull/836)

