import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Expected values, computed independently from environment/access.log
# (6 request lines; clients 192.168.0.1, 192.168.0.2, 10.0.0.5 -> 3 unique IPs;
# /index.html requested 3x, more than any other path).
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def _load_report() -> dict:
    assert REPORT_PATH.exists(), f"no report found at {REPORT_PATH}"
    assert REPORT_PATH.stat().st_size > 0, "report.json is empty"
    with open(REPORT_PATH) as f:
        return json.load(f)


def test_report_has_required_fields():
    """The report is valid JSON with the required fields and types."""
    report = _load_report()
    for field in ("total_requests", "unique_ips", "top_path"):
        assert field in report, f"report.json is missing '{field}'"
    assert isinstance(report["total_requests"], int), "total_requests must be an int"
    assert isinstance(report["unique_ips"], int), "unique_ips must be an int"
    assert isinstance(report["top_path"], str), "top_path must be a string"


def test_total_requests_is_correct():
    report = _load_report()
    assert report["total_requests"] == EXPECTED["total_requests"], (
        f"expected total_requests={EXPECTED['total_requests']}, "
        f"got {report['total_requests']}"
    )


def test_unique_ips_is_correct():
    report = _load_report()
    assert report["unique_ips"] == EXPECTED["unique_ips"], (
        f"expected unique_ips={EXPECTED['unique_ips']}, got {report['unique_ips']}"
    )


def test_top_path_is_correct():
    report = _load_report()
    assert report["top_path"] == EXPECTED["top_path"], (
        f"expected top_path={EXPECTED['top_path']!r}, got {report['top_path']!r}"
    )
