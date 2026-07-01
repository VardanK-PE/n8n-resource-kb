---
type: database
name: "<engine>-<host>-<database>"
engine: "<postgres|mysql|mongodb|mssql|snowflake|...>"
host: "<host>"
database: "<database name>"
auto_generated_at: 2026-01-01T00:00:00Z
---

<!-- auto:start -->

# Database: <engine>:<host>/<database>

- **Engine:** `<engine>`
- **Host:** `<host>`
- **Database:** `<database>`

## Tables / collections referenced

- `<table_or_collection>`
- `<table_or_collection>`

## Representative queries

```sql
-- from workflow <slug>, node "<node name>" (id <node-id>)
SELECT … FROM <table> WHERE …;
```

## Used by

- [[../../workflows/<slug>]] — node "<node name>" (id `<node-id>`)

<!-- auto:end -->

<!-- manual:start -->

<!-- DBA contact, retention policy, prod vs staging distinction, etc. -->

<!-- manual:end -->
