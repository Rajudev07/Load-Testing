import json
import os
from datetime import datetime, timezone

with open("performance/k6-summary.json", "r", encoding="utf-8") as f:
    summary = json.load(f)

metrics = summary["metrics"]

result = {
    "schema_version": "1.0",
    "provider": "github_actions",
    "repository_full_name": os.environ["GITHUB_REPOSITORY"],
    "branch": os.environ["GITHUB_REF_NAME"],
    "commit_sha": os.environ["GITHUB_SHA"],
    "github_run_id": os.environ["GITHUB_RUN_ID"],
    "environment_id": "github-hosted-er010-v1",
    "workload_id": "zeroui-er010-http-get-v1",
    "measured_at_utc": datetime.now(timezone.utc).isoformat(),
    "p95_latency_ms": metrics["http_req_duration"]["values"]["p(95)"],
    "error_rate": metrics["http_req_failed"]["values"]["rate"],
    "throughput_rps": metrics["http_reqs"]["values"]["rate"],
}

with open("er010-performance-result.json", "w", encoding="utf-8") as f:
    json.dump(result, f, indent=2)

print(json.dumps(result, indent=2))