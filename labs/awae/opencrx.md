# OpenCRX

## Random

Password reset makes it relatively easy to brute force, as the seed for the `Random` function is predictable and so is the sequence of `nextInt` calls.  Should be using `SecureRandom` instead!

```java
String resetToken = Utils.getRandomBase62(40);

changePassword((Password)loginPrincipal
          .getCredential(), null, "{RESET}" + resetToken);
```
```java
 public static String getRandomBase62(int length) {
    String alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    Random random = new Random(System.currentTimeMillis());
    String s = "";
    for (int i = 0; i < length; i++) {
      s = s + "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz".charAt(random.nextInt(62));
    }
    return s;
  }
```

## Accounts

OpenCRX has default logins:

```
guest:guest
admin-Standard:admin-Standard
admin-Root:admin-Root
```

## References

[Base62](https://en.wikipedia.org/wiki/Base62)

$P$BKTtSM4rcbQEjHNQwCiibf5nqvmSGm/