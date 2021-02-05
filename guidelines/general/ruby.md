

# File.open() vs Kernel#open()

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
