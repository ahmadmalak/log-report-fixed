import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")

# Computed independently from environment/access.log: 6 request lines;
# clients 192.168.0.1, 192.168.0.2, 10.0.0.5 -> 3 unique IPs; /index.html
# requested 3x, more than any other path.
EXPECTED = {
    "total_requests": 6,
    "unique_ips": 3,
    "top_path": "/index.html",
}


def test_report_exists_and_is_valid_json():
    """instruction.md criterion 1: /app/report.json exists and is valid JSON."""
    assert REPORT_PATH.exists(), f"no report found at {REPORT_PATH}"
    with open(REPORT_PATH) as f:
        json.load(f)  # raises if not valid JSON


def test_report_has_required_fields_with_correct_types():
    """instruction.md criterion 2: the report contains total_requests, unique_ips,
    and top_path, with the types described in the instructions."""
    with open(REPORT_PATH) as f:
        report = json.load(f)
    for field in ("total_requests", "unique_ips", "top_path"):
        assert field in report, f"report.json is missing '{field}'"
    assert isinstance(report["total_requests"], int), "total_requests must be an int"
    assert isinstance(report["unique_ips"], int), "unique_ips must be an int"
    assert isinstance(report["top_path"], str), "top_path must be a string"


def test_report_values_are_correct():
    """instruction.md criterion 3: all three values are computed correctly
    from /app/access.log."""
    with open(REPORT_PATH) as f:
        report = json.load(f)
    assert report["total_requests"] == EXPECTED["total_requests"], (
        f"expected total_requests={EXPECTED['total_requests']}, "
        f"got {report['total_requests']}"
    )
    assert report["unique_ips"] == EXPECTED["unique_ips"], (
        f"expected unique_ips={EXPECTED['unique_ips']}, got {report['unique_ips']}"
    )
    assert report["top_path"] == EXPECTED["top_path"], (
        f"expected top_path={EXPECTED['top_path']!r}, got {report['top_path']!r}"
    )
