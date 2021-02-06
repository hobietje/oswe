# Returning additional rows

A good way to get a predictable result from a SQL query to get rid of the first, i.e. expected, row of the result and then adding a predictable row using `' UNION SELECT '1`.

For example, if the developer has a query that has `column1 = '${USER_INPUT}'` then we can turn that query into `column1 = '' UNION SELECT '1'`
