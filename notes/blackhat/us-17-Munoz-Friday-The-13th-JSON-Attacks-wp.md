
Requirements for RCE from deserialization libraries:

* Attacker needs to control the type of reconstructed object, e.g. via `_type`, `$type`, `class`, `classname`, `javaClass` properties in the injected JSON
  * LOOK FOR THESE IN BURP TRAFFIC INTERCEPTED!  TODO: Find a plugin?
* Deserialization library or Garbage Collector must call methods on reconstructed object
* There must be gadget chains starting on method execution upon or after object reconstruction

Deserialization logic tends to be performed in one of two ways:

* Post-deserialization cast (cast) – JSON is deserialised (incl. RCE executing) and then attempted to be cast to specific types.   No protection at all, fails only after entire deserialization.
* Inspection of target object type (EOGI) — JSON is serialized progressively and typed objects created and setters validated and called immediately; fails early.  Attacker can use fields with an `object`, `HashTable` or simlar types to deserialize arbitrary object types that can lead to RCE.

# .NET

## Gadgets that lead to code execution

Direct RCE:

* `System.Configuration.Install.AssemblyInstaller`
  * `set_Path`
  * Path controlled by an attacker; .NET may have extra checks for remote paths
  * Execute payload on local assembly load

* `System.Activities.Presentation.WorkflowDesigner`
  * `set_PropertyInspectorFondAndColorData`
  * Arbitrary XAML load
  * Requires STA threat

* `System.Windows.ResourceDictionary`
  * `set_Source`
  * Arbitrary XAML load
  * Required to be able to work with setters of types derives from IDictionary.  Should be able to set SystemOverride type.

* `System.Windows.Data.ObjectDataProvider`
  * `set_(MethodName|ObjectInstance|ObjectType)`
  * Arbitrary Method Invocation

Arbitrary Getter call:

* `System.Windows.Forms.BindingSource`
  * `set_DataMember`


XXE:

* `System.Xml.XmlDocument` or `System.Xml.XmlDataDocument`
  * `set_InnerXml`
* `System.Data.DataViewManager`
  * `set_DataViewSettingCollectionString`


## JSON Payload


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

## Libraries

__[FastJSON](https://github.com/mgholam/fastJSON)__

Cast, vulnerable by default

```
var obj = (ExpectedType) JSON.ToObject(untrusted);
```

E.g. KalicoCMS, CVE-2017-10712

__Json.NET__ 

EOGI, only vulnerable when the `TypeNameHandling` setting is not `None`, unless `SerializationBinder` is correctly used to whitelist permitted and only safe types.

```
public class Message {
    [JsonProperty(TypeNameHandling = TypeNameHandling.All)]
    public object Body { get; set; }
}
```

E.g. Breeze (CVE-2017-9424):
* Has `TypeNameHandling.Objects` set in the global `JsonSerializerSettings`
* Deserializes user provided input to an expected type
* That expected type has a property with an `Object` type setter

__FSPickler__

EOGI, potentially vulnerable


__Sweet.Jayson_

Cast, vulnerable by default

__System.Web.Script.Serialization.JavascriptSerializer__

Secure by default, but insecure when a type resolver is used like `SimpleTypeResolver` as it will then perform a cast operation.

```
JavaScriptSerializer sr = new JavaScriptSerializer(new SimpleTypeResolver());
string reqdInfo = apiService.authenticateRequest();
reqdDetails det = (reqdDetails)(sr.Deserialize<reqdDetails>(reqdInfo))
```

__System.Runtime.Serialization.Json.DataContractJsonSerializer__

EOGI + Whitelist, mostly secure, but can still be vulnerable if an attacker can control the expected type that is whitelisted when the `DataContractJsonSerializer` object is constructed.

```
var typename = cookie["typename"];
var serializer = new DataContractJsonSerializer(Type.GetType(typename));
var obj = serializer.ReadObject(ms);
```

# Java

## Gadgets that lead to code execution

Direct RCE:

* `org.hibernate.jmx.StatisticsService`
  * `setSessionFactoryJNDIName`
  * JNDI lookup
  * TODO: Watch talk [A journey from JNDI/LDAP manipulation to Remote Code Execution](https://www.youtube.com/watch?v=Y8a5nB-vy78&ab_channel=BlackHat) at BlackHat 2016 [slides](https://www.blackhat.com/docs/us-16/materials/us-16-Munoz-A-Journey-From-JNDI-LDAP-Manipulation-To-RCE.pdf)

* `com.atomikos.icatch.jta.RemoteClient`
  * `toString`
  * JNDI lookup

* `com.sun.rowset.JbdcRowSetImpl`
  * `setAutoCommit`
  * JNDI lookup
  * Available in Java JRE

Arbirary Getting Call:

* `org.antlr.stringtemplate.StringTemplate`
  * `toString`
  * Can be used to chain to other gadgets such as the infamous `TemplatesImpl.getOutputProperties()`

## Libraries

* Jackson - EOGI, potentially vulnerable
* Genson - EOGI, potentially vulnerable
* JSON-IO - Cast, vulnerable by default
* FlexSON - Cast, vulnerable by default
* GSON - EOGI, not vulnerable

# TODO

TODO: See similar research from Moritz Bechler with different gadgets for Java in Jackson, JSON-IO, and Spring:
https://github.com/mbechler/marshalsec