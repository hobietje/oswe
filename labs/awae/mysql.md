## FYI

Can replace spaces with anything that consistutes a space substitute... that includes inline comments `SELECT/**/1`.

MySQL interprets a pound sign `#` as the start of a comment (or `%23` as a UrlEncoded value)

Use backticks `\`` to escape column or table names that are reserved in the SQL language.

## Injection

## Discovery

```sql
select version();
```

## Escalation

## Exfiltration

Check one letter at a time using a blind injection.  Convert the letter being checked to an ascii value to bypass any filters that may be in place for quotes and other special characters.

```sql
select substring(version(), 1, 1)='4';
select ascii(substring(version(), 1, 1))=52;
```

To optimise, use greater/lower than comparisons instead to exclude 50% of potential ascii codes in one request.