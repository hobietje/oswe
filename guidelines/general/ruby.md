# Unexpected Behaviours

## File.open() vs Kernel#open()

`File.open()` allows an attacker with control over the first argument to read arbitrary files.  I.e. a normal LFI scenario.

```
File.open("|/usr/bin/uname").read()
Errno::ENOENT: No such file or directory - |/usr/bin/uname
  from (irb):1:in `initialize'
  from (irb):1:in `open'
  from (irb):1
  from /usr/bin/irb:12:in `<main>'
```

`Kernel#open` however allows an attacker to run arbitrary command (by using a | before the command), which additionally allows RCE!
```
open("|/usr/bin/uname").read()
=> "Darwin\n"
```

 Examples:
 * [CVE-2017-17405](https://www.ruby-lang.org/en/news/2017/12/14/net-ftp-command-injection-cve-2017-17405/)

# Common Errors

## NoMethodError: undefined method '[]' for nil:NilClass

This means that the developer is using square bracket notation to read a property from an object, but the object is missing, or `nil`. [ref](https://rollbar.com/blog/top-10-ruby-on-rails-errors/#:~:text=2.-,NoMethodError%3A%20undefined%20method%20'%5B%5D'%20for%20nil%3ANilClass)

At the developer used square bracket notation, it’s likely that the code is digging through hashes or arrays to access properties.  We may be able to abuse this to access an object property or array element other than what the developer intended.
