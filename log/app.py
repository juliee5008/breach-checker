from datetime import datetime, timezone

from flask import Flask, jsonify, request, Response

from prometheus_client import Counter, CONTENT_TYPE_LATEST, generate_latest

app = Flask(__name__)

LICZNIK = Counter("log_attempts", "Licznik prób logowania", ["found"])

@app.post("/log")
def log_attempt():
    data = request.get_json(silent=True) or {}
    # Tylko metadane próby - usługa log nie dostaje pełnego skrótu, hasła ani dostępu do bazy
    entry = {
        "time": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "hash_prefix": str(data.get("hash_prefix", ""))[:5],
        "found": bool(data.get("found")),
    }
    print(f"log: {entry}", flush=True)

    found_val = "true" if entry["found"] else "false"
    LICZNIK.labels(found=found_val).inc()
    return jsonify({"status": "logged"}), 201

@app.get("/health")
def health():
    return jsonify({"status": "ok"})

@app.get('/metrics')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


    