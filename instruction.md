# Access Log Report

There is an Apache-style access log at `/app/access.log`. Parse it and write a
JSON summary report to `/app/report.json`.

The report must be a single JSON object with exactly these three fields:

1. `total_requests` (integer) — the total number of request lines in the log.
2. `unique_ips` (integer) — the number of distinct client IP addresses that made requests.
3. `top_path` (string) — the request path (e.g. `/index.html`) that appears most often across all requests.

Example output shape (values will differ based on the log contents):

```json
{"total_requests": 6, "unique_ips": 3, "top_path": "/index.html"}
```

## Success criteria

1. `/app/report.json` exists and is valid JSON.
2. It contains the fields `total_requests`, `unique_ips`, and `top_path`, with the types described above.
3. All three values are computed correctly from `/app/access.log`.
