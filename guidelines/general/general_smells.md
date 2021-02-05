[[ref](https://www.joelonsoftware.com/2005/05/11/making-wrong-code-look-wrong/)]

Make wrong code look wrong, using coding conventions:

- Keep functions short.
- Declare your variables as close as possible to the place where you will use them.
- Don’t use macros to create your own personal programming language.
- Don’t use goto.
- Don’t put closing braces more than one screen away from the matching opening brace.


# Exceptions

Exceptions being thrown are, effectively, an invisible `goto`, which, is even worse than a `goto` you can see.  

```
dosomething();
cleanup();
```

The only way to know that `cleanup` is definitely called is to investigate the entire call tree of `dosomething` to see if there’s anything in there, anywhere, which can throw an exception.

The possibility that `dosomething` might throw an exception means that `cleanup` might not get called. 

That’s easily fixable, using `finally`.

Exceptions are fine for quick-and-dirty code, for scripts, and for code that is neither mission critical nor life-sustaining. But if you’re writing an operating system, or a nuclear power plant, or the software to control a high speed circular saw used in open heart surgery, exceptions are extremely dangerous.

TODO [http://blogs.msdn.com/oldnewthing/archive/2005/01/14/352949.aspx](http://blogs.msdn.com/oldnewthing/archive/2005/01/14/352949.aspx)

# Code Control Macros

TODO [http://blogs.msdn.com/oldnewthing/archive/2005/01/06/347666.aspx](A rant against flow control macros)

“When you see code that uses [macros], you have to go dig through header files to figure out what they do.”