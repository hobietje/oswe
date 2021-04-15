# AWAE/OSWE

This repository is to keep any scripts, notes, etc from my AWAE course and for the OSWE exam preparation in one place.  Some of these resources are likely (even more) useful to students of the OSCP as well.

_I did not include resources related to learning the basics of various programming languages or frameworks you may encounter in the AWAE, but rather those relating to specific security flaws, exploits, bypasses, misconfigurations, etc._

# Preparation

## Course materials

Read, read, then read some more:

* AWAE course notes [TODO]
* [Code Audits 1 - Fall 2011](https://vimeo.com/30001189) and [Code Audits 2 - Fall 2011](https://vimeo.com/29702192)

  Somewhat dated and focussed on C/C++, but still found it to be useful. See [my notes](guidelines/code_review.md).
* [Auditing Source](https://trailofbits.github.io/ctf/vulnerabilities/source.html) [TODO]
* Bug bountry reports [TODO]

## Practice

AWEA is hands-on, so spend tons of time doing actual code reviews.

### Labs

* [AWAE](https://www.offensive-security.com/awae-oswe/)
  
  [TODO]
  
* [PortSwigger Web Academy](https://portswigger.net/web-security)
  
  A beautifully put together set of course materials and related labs for web related vulnerabilities.  You should finish all of these :)

*  [PentesterLab PRO](https://pentesterlab.com/referral/Li4afWlMWsD9Sg)
    
    Love.  I preferred to work on each topic area and ignored the Badges, e.g. doing every JWT lab available in sequence.  I felt this helped me to continue diving deeper into one topic area without frequent context switching.  These are probably most appropriate for the AWAE/OSWE:
    
    * The [CGI](labs/pentesterlab.com/cgi.md) labs for Shellshock and similar issues
    * All [JWT](labs/pentesterlab.com/jwt.md) labs for auth bypasses

### Known vulnerable apps

Perform code reviews (not black box pen testing!) on:

* OWASP Juice Box [TODO]
* Damn Vulnerable Web Application [TODO]

### Open source code

Plenty of OSS out there, but I spent some time trying to find known vulnerabilities in old versions of these:

* [ImpressCMS](https://github.com/ImpressCMS/impresscms)

## Tooling

Debuggers:

* TODO

Disassemblers:

* TODO

Code review tools:

* [graudit](automation/graudit/README.md) to quickly find potentially sensive parts of the code, to be investigated as part of a manual review.

Runtime AST:

* [wfuzz](automation/wfuzz/README.md) to be able to quickly scan/fuzz web servers for interesting endpoints and potential weaknesses.
* [aquatone](automation/aquatone/README.md) to be grab screenshots of websites.

Evil Payloads:

* [jwt](automation/jwt/README.md) to generate or tamper with JWTs to bypass authn/authz.

Other:

* [john](automation/john/README.md) to brute force potential password hashes discovered.

# Other resources & references

Where possible, I reference specific write-ups, presentations, etc in my vulnerability or language specific notes.

These are some additional reference sets that I have found useful to define my own learning roadmap:

1. [deletehead/awae_oswe_prep](https://github.com/deletehead/awae_oswe_prep)

    Discusses a study strategy and the AWAE syllabus; otherwise didn't find it to have many useful links or tips.

1. [wetw0rk/AWAE-PREP](https://github.com/wetw0rk/AWAE-PREP)

    Mixture of links to "learn to code" courses, but also some good vulnerability labs and write-ups that I used.

# Wordlists

Might come in handy to fuzz web endpoints, passwords, LFI/RFI, etc:

1. [wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist)