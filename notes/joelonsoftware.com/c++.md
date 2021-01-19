# Operator overloading [[ref](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/)]

```
i = j * 5;
```

In C you know, that j is being multiplied by five and the results stored in i.  But if you see that same snippet of code in C++, you don’t know anything.

The only way to know what’s really happening in C++ is to find out what types i and j are, something which might be declared somewhere altogether else. That’s because j might be of a type that has operator* overloaded and it does something terribly witty when you try to multiply it.

 The only way to find out is not only to check the type of the variables, but to find the code that implements that type, and God help you if there’s inheritance somewhere, because now you have to traipse all the way up the class hierarchy all by yourself trying to find where that code really is, and if there’s polymorphism somewhere, you’re really in trouble because it’s not enough to know what type i and j are declared, you have to know what type they are right now, which might involve inspecting an arbitrary amount of code and you can never really be sure if you’ve looked everywhere thanks to the halting problem (phew!).