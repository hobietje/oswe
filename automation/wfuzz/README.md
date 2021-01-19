# Wfuzz

See [Source](https://github.com/xmendez/wfuzz) & [Documentation](https://wfuzz.readthedocs.io/en/latest/)

# Use Cases

Fuzz HTTP/S endpoints for interesting responses, e.g.:

  * response to different HTTP methods (general/http_methods.txt)
  * common admin panels (general/adminpanels.txt)
  * common technology specfic pages and vulns (vulns/*.txt)
  * common web service endpoints and apis (webservices/ws-dirs.txt)

```
wfuzz -w wordlist/general/common.txt --hc 404 http://testphp.vulnweb.com/FUZZ
```

Generate payloads

```
wfpayload -z range,0-10
0
1
2
3
4
5
6
7
8
9
10
```

Encode or decode data

```
wfencode -e md5 test
098f6bcd4621d373cade4e832627b4f6
```