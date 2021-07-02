# AWAE/OSWE

This repository is to keep any scripts, notes, etc from my AWAE course and for the OSWE exam preparation in one place.  Some of these resources are likely (even more) useful to students of the OSCP as well.

_I did not include resources related to learning the basics of various programming languages or frameworks you may encounter in the AWAE, but rather those relating to specific security flaws, exploits, bypasses, misconfigurations, etc._

# Preparation

OWSE is a hands-on exam that is a __white-box__ assessment of __web applications__.  As a result, you should focus your efforts on:

1. Becoming familiar with __common web application vulnerabilities__

    What they are, how to spot them in code, how to exploit them

2. Establishing a repeatable __methodology__ to audit a web application code base...

    What are it's features, what user privilege levels exist, what technology is in use, is it subject to SQLi? Mayble XSS? Or Auth Bypass? IDOR/BOLA or mass assignment? Deserialization? Malicious file uploads? LFI/RFI? etc

3. Doing actual __code reviews__ to find vulnerabilties

    Practice, practice, practice.  Find potentially vulnerable code, trace the data sources and sinks to verify it is exploitable, understand any filters or other mechanisms you need to bypass to reach the vulnerable code

3. Writing your own __exploits__ for said vulnerabilties

    Get familiar with hand-crafting your exploits, most likely in Python but whatever suits your fancy.  Make GET/POST requests, upload files, parse responses, deal with sessions and cookies.

## Common Web App Vulnerabilities

Read, read, then read some more:

* AWAE course notes

  Read all course notes and/or watch the videos. Also send extra time to read up on all the linked/referenced materials that have more details on specific vulnerabilties, frameworks, etc.

* [The Tangled Web: A Guide to Securing Modern Web Applications](https://www.amazon.com/Tangled-Web-Securing-Modern-Applications/dp/1593273886) and [The Web Application Hacker's Handbook: Finding and Exploiting Security Flaws](https://www.amazon.com/Web-Application-Hackers-Handbook-Exploiting/dp/1118026470)

  Very comprehensive books on web application security... definitely worth getting one of these prior to the OSWE if you aren't that familiar with web apps.

* [OWASP Top 10](https://owasp.org/www-project-top-ten/)

  The most commonly seen web application vulnerabilities. Learn what they are and how to spot them and lack of mitigating controls in the code.

* [Code Audits 1 - Fall 2011](https://vimeo.com/30001189) and [Code Audits 2 - Fall 2011](https://vimeo.com/29702192)

  Somewhat dated and focussed on C/C++, but still found it to be useful. See [my notes](guidelines/code_review.md).

* Bug bountry reports

  I keep an eye on interesting bounty reports as a general practice.  

## Methodologies

Find a methodology that works for you to systematically review an application.  You can get inspiration for your methodology items or checklist from:

* AWAE course syllabus

  Make sure all the key vulnerabilty classes from the course syllabus are included in your test methodology.  __You _KNOW_ these are the scope of the exam, so make sure you don't forget to check for an entire class of vulnerabilities!__

* [OWASP Top 10](https://owasp.org/www-project-top-ten/)

  You should do a review for these items. Find all potentially vulnerable functions within the code and trace their sources/sinks to see if they are exploitable.

* [OWASP Secure Coding Practices,
Quick Reference Guide](https://owasp.org/www-pdf-archive/OWASP_SCP_Quick_Reference_Guide_v2.pdf)

  The checklist itself is too detailed and overkill for OWSE imo (and due to time constraints probably most real-life code reviews as well?), however the broad categories of items are extremely useful.  Looks for issues in the code that indicate poorly implemented authentication, missing authorization, bad session management, predictable random number generation, etc and see if any of them can help lead to an exploit.

* [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/stable/)

  Probably the most complete "bible" of checks to perform during web application testing, but similar to the earlier checklist too comprehensive for OWSE.  Again, make note of the broad categories of checks and come back for more detail if needed.

During the assessment, maintain documentation of what you have reviewed and what's left to loop back on.  I keep my documentation fairly lightweight in a set of markdown files, one for each area of review (e.g. app feature, vulnerability class).  I find markdown works well as it can include code blocks with syntax highlighting, while keeping other formatting efforts to a minimum.

## Code Reviews

They key component of the OSWE is about performing a white box code review of an application.  As such, you need to practice this skill hands-on as much as possible:

* [AWAE](https://www.offensive-security.com/awae-oswe/)

  The AWAE course itself provides several walkthroughs of vulnerabilities.  I found these useful to learn about the vulnerability classes and understand the related code.  
  
  Unfortunately, these provide you the "answer" on a silver platter and don't require you to review most of the code.  You don't need to discover the existence of these vulnerabilities inside a large codebase.
  
  Luckily, the [AWAE](https://www.offensive-security.com/awae-oswe/) course _does_ provide 3 additional undocumented applications (Answers, DocEdit, Sqeakr). Imo, theseare the most useful components of the course and I cannot encourgage you enough to complete these as __they give you the exact experience you will get on the exam__.

* [PortSwigger Web Academy](https://portswigger.net/web-security)
  
  This is a beautifully put together set of course materials and related exploitation labs for web related vulnerabilities.  These are black box exercises, but I still recommend you finish all of these!

* [PentesterLab PRO](https://pentesterlab.com/referral/Li4afWlMWsD9Sg)
  
  Similar to PortSwigger Web Academy, but learning from historical CVEs rather than vulnerability classes.  I preferred to work on each topic area and ignored the "Badges", i.e. I did all SQLi related lab in one hit as this helped me to deep dive into one topic area without frequent context switching. 
  
  Pick the labs related to OSWE topics (SQLi, SSTI, Deserialization, ...) but ignore others until you have more time (PCAP, JWT, SAML, ...).  I spent time on the latter which was definitely educational but not helpful for the OSWE specifically.

* Review known vulnerable apps

  Perform code reviews (not black box pen testing!) on purpose built vulnerable apps like:

  * [OWASP Juice Box](https://owasp.org/www-project-juice-shop/)
  * [Damn Vulnerable Web Application](https://dvwa.co.uk/)
  * [OWASP Broken Web Apps](https://code.google.com/p/owaspbwa/)
  * ...

* Re-discover vulnerabilities in OSS

  There is a huge history of vulnerabilities in older versions of open source software.  Download older known versions and see if you can rediscover the same vulnerability with no/minimal assistance.  E.g.:

  * [ImpressCMS](https://github.com/ImpressCMS/impresscms)
  * [Wordpress](https://en-au.wordpress.org/download/)
  * [DotNetNuke](https://www.dnnsoftware.com/)
  * ...

## Exploits

Unlike the OSCP, where you use existing exploits, the OSWE requires you to write all your own exploit code.  You will need to become familiar with Python or another language of your choice. I have a software development background so didn't focus too much on this, however I did still:

* Code up all the course exercises and extra miles.  

  Having code to copy-paste or at least refer to during the exam is a huge time saver. Most (if not all) exploit code needed for the exam has a similar exploit somewhere in the course that can be tweaked.

* Write my own scripts for brute forcing and data exfiltration.

  OSWE doesn't allow you to use most security automation and fuzzing tools... E.g. no _sqlmap_!  Do you really want to figure out how to write code for a UNION-based, time-based, blind, or another type of SQLi data exfiltration during your precious 48hr exam period?

* Create customised wordlists for fuzzing LFI, injections, etc.

  Definitely keep wordlists like [SecLists](https://github.com/danielmiessler/SecLists) handy, use lists included with tools like
  [wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist) and review sensitive code keyword lists from [graudit](https://github.com/wireghoul/graudit), but don't stop there...  Start compiling your own lists of sensitive code statements, SQL and other injections, default passwords, paths to DB/Web/OS configuration files (LFI), etc.

# Post-Exam Review

Your mileage will likely vary as these are heavily influenced  by my prior knowledge and skills, but If I had to do it all over again I would make sure to:

* Avoid spending time on off-syllabus topics

  I spent a lot of time doing exercises on JWT vulnerabilities, which do fall within a "web application" security assessement scope, but aren't part of the AWAE syllabus. :(

* Similarly, avoid learning to use "not permitted during the exam" tools

  I similarly spent time learning how to use some security tools that turned out to be forbidden for use during the exam. :(

* Spend more time practicing

  Do actual white-box code reviews rather than merely _reading about_ doing white-box code reviews.

* Spend less time (re-)learning about vulnerability classes that were (to a lesser extent) already covered in OSCP or my other prior learnings

  I already had plenty of prior knowledge on certain vulnerability classes and could have easily skipped or skimmed certain sections of the AWAE videos and course materials.

* Establish and improve my code review methodology through repeat practice.  Then, boil down that methodology to a small checklist specifically tailored for the exam based on the course syllabus.

  I didn't have a sufficiently mature methodology going into the exam.  On one of the questions I hit a dead end repeatedly revisited the same vulnerability classes over and over again, thinking I had missed something, but without success.  Only after reviewing the course syllabus for inspiration during an exam break did I realise I had missed an entire vulnerability class.  :(

# References

These are some additional reference sets that I used to define my own learning roadmap:

1. [deletehead/awae_oswe_prep](https://github.com/deletehead/awae_oswe_prep)

    Discusses a study strategy and the AWAE syllabus; otherwise didn't find it to have many useful links or tips.

1. [wetw0rk/AWAE-PREP](https://github.com/wetw0rk/AWAE-PREP)

    Mixture of links to "learn to code" courses, but also some good vulnerability labs and write-ups that I used.
