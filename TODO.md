# TODO

## Familiarize with tools

Notepad++ searching capabilities
dnSpy
regex101.com
JD-GUI

## References

__AWAE specific guides__

1. [Friday the 13th: JSON Attacks](https://www.youtube.com/watch?v=oUAeWhW5b8c&ab_channel=BlackHat)

1. [AWAE Prep](https://github.com/wetw0rk/AWAE-PREP)

    * XSS and MySQL	Challenge	https://www.vulnhub.com/entry/pentester-lab-xss-and-mysql-file,66/
    * Understanding PHP Object Injection	Tutorial	https://securitycafe.ro/2015/01/05/understanding-php-object-injection/
    * /dev/random: Pipe	Challenge	https://www.vulnhub.com/entry/devrandom-pipe,124/
    * Understanding Java Deserialization	Tutorial	https://nytrosecurity.com/2018/05/30/understanding-java-deserialization/
    * Practicing Java Deserialization Exploits	Challenge/Tutorial	https://diablohorn.com/2017/09/09/understanding-practicing-java-deserialization-exploits/
    * SQL Injection Attacks and Defense	Book	https://www.amazon.com/Injection-Attacks-Defense-Justin-Clarke/dp/1597499633

1. [AWAE/OSWE](https://github.com/timip/oswe)

    Links for exploit-db/github in repo for each of the AWAE exercises.

__Code security review guidelines__

1. [OWASP Code Review Guide](https://owasp.org/www-pdf-archive/OWASP_Code_Review_Guide-V1_1.pdf)

__Vulnerability write-ups__

1. [Just Another Hacker (Wireghaul)](http://archive.justanotherhacker.com/)

1. https://www.nccgroup.com/au/about-us/newsroom-and-events/blogs/2019/august/getting-shell-with-xamlx-files/

__Deserialization__

1. See similar research from Moritz Bechler with different gadgets for Java in Jackson, JSON-IO, and Spring:
https://github.com/mbechler/marshalsec

1. https://frohoff.github.io/appseccali-marshalling-pickles/

1. https://www.rsaconference.com/writable/presentations/file_upload/asd-f03-serial-killer-silently-pwning-your-java- endpoints.pdf

1. https://community.saas.hpe.com/t5/Security-Research/The-perils-of-Java-deserialization/ba- p/246211#.WVIMyROGPpQ

1. https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE- wp.pdf

1. http://www.newtonsoft.com/json/help/html/SerializationErrorHandling.htm

1. https://cheatsheetseries.owasp.org/cheatsheets/Deserialization_Cheat_Sheet.html

1. https://book.hacktricks.xyz/pentesting-web/deserialization

  - JSON
  – XML / SOAP
  – YAML
  – Binary Java Objects
  – Binary .NET Objects
  – Pickle (Python Binary Objects)
  – WCF Compact Binary

1. https://foxglovesecurity.com/2015/11/06/what-do-weblogic-websphere-jboss-jenkins-opennms-and-your-application-have-in-common-this-vulnerability/

1. https://github.com/GrrrDog/Java-Deserialization-Cheat-Sheet

1. https://www.slideshare.net/codewhitesec/java-deserialization-vulnerabilities-the-forgotten-bug-class

1. https://www.slideshare.net/joaomatosf_/an-overview-of-deserialization-vulnerabilities-in-the-java-virtual-machine-jvm-h2hc-2017

__.NET Gadgets__

1. https://github.com/pwntester/ysoserial.net

__2FA/OTP Bypass__

1. https://book.hacktricks.xyz/pentesting-web/2fa-bypass

__Abusing hop-by-hop headers__

1. https://book.hacktricks.xyz/pentesting-web/abusing-hop-by-hop-headers

__Bypass Payment Process__

1. https://book.hacktricks.xyz/pentesting-web/bypass-payment-process

__Captcha Bypass__

1. https://book.hacktricks.xyz/pentesting-web/captcha-bypass

__Cache Poisoning and Cache Deception__

1. https://book.hacktricks.xyz/pentesting-web/cache-deception

__Clickjacking__

1. https://book.hacktricks.xyz/pentesting-web/clickjacking

__Client Side Template Injection (CSTI)__

1. https://book.hacktricks.xyz/pentesting-web/client-side-template-injection-csti

__Command Injection__

1. https://book.hacktricks.xyz/pentesting-web/command-injection

__CSP Bypass__

1. https://book.hacktricks.xyz/pentesting-web/content-security-policy-csp-bypass

__Cookies__

1. https://book.hacktricks.xyz/pentesting-web/hacking-with-cookies

__CORS Bypass__

1. https://book.hacktricks.xyz/pentesting-web/cors-bypass

__CRLF Injection__

1. https://book.hacktricks.xyz/pentesting-web/crlf-0d-0a

__Cross-site WebSocket Hijacking__

1. Cross-site WebSocket hijacking (CSWSH)

__CSRF (Cross Site Request Forgery)__

1. https://book.hacktricks.xyz/pentesting-web/csrf-cross-site-request-forgery

__Dangling Markup - HTML scriptless injection__

1. https://book.hacktricks.xyz/pentesting-web/dangling-markup-html-scriptless-injection

__Domain/Subdomain takeover__

1. https://book.hacktricks.xyz/pentesting-web/domain-subdomain-takeover

__Email Header Injection__

1. https://book.hacktricks.xyz/pentesting-web/email-header-injection

__File Inclusion/Path traversal__

1. https://book.hacktricks.xyz/pentesting-web/file-inclusion

__File Upload__

1. https://book.hacktricks.xyz/pentesting-web/file-upload

__Formula Injection__

1. https://book.hacktricks.xyz/pentesting-web/formula-injection

__HTTP Request Smuggling / HTTP Desync Attack__

1. https://book.hacktricks.xyz/pentesting-web/http-request-smuggling

__IDOR__

1. https://book.hacktricks.xyz/pentesting-web/idor

__JWT__

1. https://book.hacktricks.xyz/pentesting-web/hacking-jwt-json-web-tokens

__NoSQL Injection__

1. https://book.hacktricks.xyz/pentesting-web/nosql-injection

__LDAP Injection__

1. https://book.hacktricks.xyz/pentesting-web/ldap-injection

__OAuth to Account takeover__

1. https://book.hacktricks.xyz/pentesting-web/oauth-to-account-takeover

__Open Redirect__

1. https://book.hacktricks.xyz/pentesting-web/open-redirect

__Parameter Pollution__

1. https://book.hacktricks.xyz/pentesting-web/parameter-pollution

__PostMessage Vulnerabilities__

1. https://book.hacktricks.xyz/pentesting-web/postmessage-vulnerabilities

__Race Condition__

1. https://book.hacktricks.xyz/pentesting-web/race-condition

__Rate Limit Bypass__

1. https://book.hacktricks.xyz/pentesting-web/rate-limit-bypass

__SQL Injection__

1. https://book.hacktricks.xyz/pentesting-web/sql-injection

__SSRF (Server Side Request Forgery)__

1. https://book.hacktricks.xyz/pentesting-web/ssrf-server-side-request-forgery

__SSTI (Server Side Template Injection)__

1. https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection

__Unicode Normalization vulnerability__

1. https://book.hacktricks.xyz/pentesting-web/unicode-normalization-vulnerability

__XPath Injection__

1. https://book.hacktricks.xyz/pentesting-web/xpath-injection

__XSLT Server Side Injection (Extensible Stylesheet Languaje Transformations)__

1. https://book.hacktricks.xyz/pentesting-web/xslt-server-side-injection-extensible-stylesheet-languaje-transformations

__XXE - XEE - XML External Entity__

1. https://book.hacktricks.xyz/pentesting-web/xxe-xee-xml-external-entity

__XSS (Cross Site Scripting)__

1. https://book.hacktricks.xyz/pentesting-web/xss-cross-site-scripting

__XSSI (Cross-Site Script Inclusion)__

1. https://book.hacktricks.xyz/pentesting-web/xssi-cross-site-script-inclusion

__XS-Search__

1. https://book.hacktricks.xyz/pentesting-web/xs-search

__Reset/Forgoten Password Bypass__

1. https://book.hacktricks.xyz/reset-password