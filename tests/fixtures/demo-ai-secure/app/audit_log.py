"""Journal d'audit structuré (append-only) des traitements d'IA."""
import json
import time
import uuid
from pathlib import Path

AUDIT_LOG_PATH = Path("var/audit_log.jsonl")


def log_event(event_type: str, **fields) -> str:
    trace_id = str(uuid.uuid4())
    record = {"trace_id": trace_id, "ts": time.time(), "event": event_type, **fields}
    AUDIT_LOG_PATH.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_LOG_PATH.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, ensure_ascii=False) + "\n")
    return trace_id
