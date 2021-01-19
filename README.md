# AWAE/OSWE

This repository is to keep any scripts, notes, etc from my AWAE course and for the OSWE exam preparation.

I did not include resources related to learning the basics of various programming languages or frameworks you may encounter in the AWAE, but rather those relating to common security flaws, exploits, bypasses, misconfigurations, etc.

# Preparation

## AWAE course notes and videos

## Familiarize with debuggers and other toools

## Practice on AWAE labs

## Practice on real-life Open Source

## Review bug bountry reports

## Automation for discovery

Code review:

* [graudit](automation/graudit/README.md) to quickly find potentially sensive parts of the code, to be investigated as part of a manual review.

Runtime AST:

* [wfuzz](automation/wfuzz/README.md) to be able to quickly scan/fuzz web servers for interesting endpoints and potential weaknesses.

Other:

* [john](automatoin/john/README.md) to brute force potential password hashes discovered.

# Resources & references

Where possible, I reference specific write-ups, presentations, etc in my vulnerability or language specific notes.

These are some more general reference sets that I have found useful to define my own learning roadmap:

1. [deletehead/awae_oswe_prep](https://github.com/deletehead/awae_oswe_prep)

    Discusses a study strategy and the AWAE syllabus; otherwise has limited useful links to resources nor tips.

1. [wetw0rk/AWAE-PREP](https://github.com/wetw0rk/AWAE-PREP)

    Mixture of links to "learn to code" courses, but also some good vulnerability labs and write-ups that I used.

# Wordlists

1. [wfuzz](https://github.com/xmendez/wfuzz/tree/master/wordlist)