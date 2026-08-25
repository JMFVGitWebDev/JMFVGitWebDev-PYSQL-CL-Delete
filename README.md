# Background

SQL sublanguage: DML (Data Manipulation Language)

The "DELETE" keyword is utilized to remove records based on a condition.

DELETE FROM table_name WHERE condition;

NOTE: Whenever you execute a DELETE statement, have a WHERE condition that identifies exactly what records you
would like to delete. Leaving this out will remove ALL records from the table.

## Problem 1

Assume the following table already exists.

| id  | firstname |
| --- | --------- |
| 1   | Steve     |
| 2   | Alexa     |
| 3   | Steve     |
| 4   | Brandon   |
| 5   | Adam      |

Write the SQL command in `problem1.sql` to delete 'Steve' from the `site_user` table.

> **Note:** always wrap string values in single quotes (`' '`), not double quotes (`" "`). In standard
> SQL, double quotes are reserved for identifiers (table/column names), while single quotes are for string
> literals. SQLite happens to tolerate a double-quoted value like `" "` as a fallback when no matching
> identifier exists, so a statement written that way may still work here, but the same statement will raise an
> error on most other databases (PostgreSQL, MySQL, SQL Server, etc.), so it's best to build the correct habit
> now.
