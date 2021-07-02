## Debugging

Release builds often do not allow breakpoints to be set or won't show the contents of variables that exist.  We can recompile an assembly using `dnSpy` to remove these limitations:

* Edit Assembly Attributes
* Change the `Debuggable` attribute to include the `Default`, `DisableOptimisations`, `IgnoreSymbolStoreSequencePoints`, `EnableEditAndContinue` flags
* Save the edited assembly

Note that IIS workers need to be reloaded for changed to be picked up, as assemblies are cloned to a temp path at runtime.

We can then attach the `dnSpy` debugger to `w3wp.exe` and pause execution from the Debug menu, view the modules loaded, and add them to the Assembly Explorer to browse the code and set breakpoints.

## Remote Debugging



## Code Smells

`Server.Transfer(...)` can allow unexpected side-effects due to the non-linear execution flow of requests, e.g. authn/z can potentially be bypassed, or input filters.

`Context.User = ...` being assigned might result in the `IsAuthenticated` condition of an authentication check reporting `true` unexpectedly (as it simply checks for it being `null` rather than a legitimate/expected user).

## Deserialization Flaws

_Typically found in PHP or Java applications, but can also occur in .NET and others._

Gadgets:

1. The class needs to be deserializable using our XmlSerializer or equivalent class
2. The class needs to execute code during the deserialization process that is of use to us
3. The class needs to be present in a loaded (or loadable?) assembly of the current .NET application

E.g.:

* DotNetNuke has a `FileSystemUtils.PullFile()` that could be useful, but XmlSerializer cannot invoke the method directly.
* .NET has an `System.Windows.Data.ObjectDataProvider` class in the `PresentationFramework` assembly, which takes `MethodName` and `MethodParameters` properties.  It can therefore be used to call the DotNetNuke `FileSystemUtils.PutFile()` method (or other useful equivalents).  Unfortunately this does not work because the default serializer expects both classes to live in the same assembly.
* `System.Data.Services.Internal.ExpandedWrapper<A,B>` can be used to work around this, by using an instance of `ExpandedWrapper` to force references to both the `FileSystemUtils` and `ObjectDataProvider` to be loaded and resolved correctly.