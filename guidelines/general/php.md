
# Comparison Operators

Sample vulnerabilities:

* [ImpressCMS: more strict comparison of variables](https://github.com/ImpressCMS/impresscms/pull/810/files)

## Type Juggling

In security sensitive features (e.g. hashes, passwords, usernames, auth checks, etc), look for inappropriate loose comparisons, where one variable is automatically cast to a different type.

In particular, these will perform type juggling and may be unsafe:

* Equal: `$a == $b`
* Not Equal: `$a != $b` or `$a <> $b`

Common mistakes occur because:

* If both operands are numeric strings `"123" == " 123"`, or one operand is a number and the other one is a numeric string `123 == " 123"`, then the comparison is done _numerically_. 
  * `"some string" == 0` returns `TRUE`. Any string that does not start with a number, when casted to an integer, will be 0.
  * `"123" == 0` returns `FALSE`
  * `"123" == " 123"` returns `TRUE`
  * `"123" == "\n123"` returns `TRUE`
  * `"123" == "123 "` returns `FALSE`!
  * `"123" == "123\n"` returns `FALSE`!
  * `'1e3' == '1000'` returns `TRUE`
  * `'+74951112233' == '74951112233'` returns `TRUE`
  * `'00000020' == '0000000000000000020'` returns `TRUE`
  * `'0X1D' == '29E0'` returns `TRUE`
  * `'0xafebac' == '11529132'` returns `TRUE`
  * `'0xafebac' == '0XAFEBAC'` returns `TRUE`
  * `'0xeb' == '+235e-0'` returns `TRUE`
  * `'0.235' == '+.235'` returns `TRUE`
  * `'0.2e-10' == '2.0E-11'` returns `TRUE`
  * `'61529519452809720693702583126814' == '61529519452809720000000000000000'` returns `TRUE` in PHP < 5.4.4.  This is on a 32-bit machine, on a 64-bit, you will have to make the strings longer.
* HTML Forms do not pass integers, floats, or booleans; they pass strings. 
* Simply doing `if ($x)` while `$x` is undefined will generate an error of level E_NOTICE.
* Some numeric operations can result in a value represented by the constant NAN. Any loose or strict comparisons of this value against any other value, including itself, but except true, will have a result of false.  
  * `NAN != NAN and NAN !== NAN`
  * Examples of operations that produce NAN include sqrt(-1), asin(2), and acosh(0)

See [Comparison Operators](https://www.php.net/manual/en/language.operators.comparison.php) for details.

## Type Comparisons

Unexpected results from operators can also occur when complex types are evaluated.  The [type comparison tables](https://www.php.net/manual/en/types.comparisons.php) provides a detailed view on how each type is compared with the same or other types.

In particular, the spaceship operator `$a <=> $b` may cause unexpected results if keys can be added or removed from object being compared, as keys are expected to match.

```php
// Objects
$a = (object) ["a" => "b"]; 
$b = (object) ["a" => "b"]; 
echo $a <=> $b; // 0
 
$a = (object) ["a" => "b"]; 
$b = (object) ["a" => "c"]; 
echo $a <=> $b; // -1
 
$a = (object) ["a" => "c"]; 
$b = (object) ["a" => "b"]; 
echo $a <=> $b; // 1
 
// not only values are compared; keys must match
$a = (object) ["a" => "b"]; 
$b = (object) ["b" => "b"]; 
echo $a <=> $b; // 1
```

For loose equality `==` or inequality comparisons `!=, <>`, the type of the left operator is most important and causes alternate logic to be used:

* An array with fewer members is smaller, if key from left-operand is not found in right-operand then arrays are uncomparable, otherwise - compared value by value
* left-operand object is always greater
* left-operand array is always greater
* left-operand boolean or `null` value will convert both sides to boolean, where `false < true`

**PHP < 8.0.0**

Prior to PHP 8.0.0, if a string is compared to a number or a numeric string then the string was converted to a number before performing the comparison. This can lead to surprising results as can be seen with the following example:

```php
var_dump(0 == "a"); // 0 == 0 -> true
var_dump("1" == "01"); // 1 == 1 -> true
var_dump("10" == "1e1"); // 10 == 10 -> true
var_dump(100 == "1e2"); // 100 == 100 -> true
```

## Floats

Because of the way floats are represented internally, you should not test two floats for equality.

## Maths

`min(-100, -10, NULL, 10, 100)` is `NULL`

## Strings

If both operands are numeric strings `"123" == " 123"`, or one operand is a number and the other one is a numeric string `123 == " 123"`, then the comparison is done _numerically_. 

Simple comparisons on strings are done by converting to numbers and applying standard math operations.  This means that they are _not_ Unicode safe!  Dedicated string comparison functions should be used:

* strcasecmp()
* strcmp()

String concatenation takes precedence over other operators.

```
```

## Ternary Operator 

Using the ternary operator shorthand, you can omit the 2nd expression.  If the 1st expression is `TRUE`, it's value is returned.  There could be a timing bug or other consequence of the difference in caching behaviour change in PHP 5.3:

```php
// Before 5.3 (or not using the shorthand)
$val = f('x') ? f('x') : false;
// f('x') will be run twice, if it evaluates to TRUE on the first call

// After 5.3
$val = f('x') ?: false;
// f('x') will only be run once
```

**PHP < 8.0.0**

Prior to PHP 8.0.0, ternary expressions were evaluated from left to right, instead of right to left like most other programming languages.

```php
// on first glance, the following appears to output 'true', however this would return 't' instead
echo (true?'true':false?'t':'f');

// the evaluation is as follows in PHP < 8.0.0:
//   echo ((true ? 'true' : false) ? 't' : 'f');
// > echo ('true' ? 't' : 'f');
// > echo ((bool)true ? 't' : 'f');
// > echo ('t');
```

# Filters

Filters a variable with a specified filter:

* If `$filter` is omitted, FILTER_DEFAULT will be used, which is equivalent to FILTER_UNSAFE_RAW.

```php
filter_var ( mixed $value , int $filter = FILTER_DEFAULT , array|int $options = 0 ) : mixed
```

## Validate filters

The function will not validate "not latin" domains.

```php
if (filter_var('уникум@из.рф', FILTER_VALIDATE_EMAIL)) {
    echo 'VALID';
} else {
    echo 'NOT VALID';
}
```

FILTER_VALIDATE_URL does not support internationalized domain name (IDN). Valid or not, no domain name with Unicode chars on it will pass validation.

I found some addresses that FILTER_VALIDATE_EMAIL rejects, but RFC5321 permits:
```php
<?php
foreach (array(
    'localpart.ending.with.dot.@example.com', // is not valid
    '(comment)localpart@example.com', // is not valid
    '"this is v@lid!"@example.com', // is not valid
    '"much.more unusual"@example.com', // is not valid
    'postbox@com', // is not valid
    'admin@mailserver1', // is not valid
    '"()<>[]:,;@\\"\\\\!#$%&\'*+-/=?^_`{}| ~.a"@example.org', // is not valid
) as $address) {
    echo filter_var($address, FILTER_VALIDATE_EMAIL);
}
?>
```


note that FILTER_VALIDATE_BOOLEAN tries to be smart, recognizing words like Yes, No, Off, On, both string and native types of true and false, and is not case-sensitive when validating strings.
```php
$vals=array('on','On','ON','off','Off','OFF','yes','Yes','YES',
'no','No','NO',0,1,'0','1','true',
'True','TRUE','false','False','FALSE',true,false,'foo','bar');
foreach($vals as $val){
    echo var_export($val,true).': ';   var_dump(filter_var($val,FILTER_VALIDATE_BOOLEAN,FILTER_NULL_ON_FAILURE));
}
```

These are also a valid urls.  This can result in an XSS vulnerability.

```
http://example.com/"><script>alert(document.cookie)</script>
http://example.ee/sdsf"f
```

FILTER_VALIDATE_URL allows this, where the %0A (URL encoded newline), in certain contexts, will split the comment from the JS code.  This can result in an XSS vulnerability.

```php
filter_var('javascript://comment%0Aalert(1)', FILTER_VALIDATE_URL);
```


Here's a simple test using filter_var with FILTER_VALIDATE_URL.

```php
$url = 'a://google.com';
$result = filter_var($url, FILTER_VALIDATE_URL); // valid
```


## Sanitize filters
## Other filters
## Filter flags