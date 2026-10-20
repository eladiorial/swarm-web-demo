
from flask import Flask, request
import socket
import os
from datetime import datetime, timezone

app = Flask(__name__)

@app.get("/")
def index():
    hostname = socket.gethostname()
    version = os.getenv("APP_VERSION", "1.0")

    return f"""
    <!doctype html>
    <html lang="gl">
    <head>
        <meta charset="utf-8">
        <meta http-equiv="refresh" content="3">
        <title>Demo Docker Swarm</title>
        <style>
            body {{ font-family: sans-serif; margin: 50px; }}
            .card {{ padding: 24px; border: 1px solid #ccc;
                     border-radius: 12px; max-width: 600px; }}
            code {{ background: #eee; padding: 5px; }}
        </style>
    </head>
    <body>
      <div class="card">
        <h1>Demo Docker Swarm</h1>
        <p>Aplicación web funcionando correctamente.</p>
        <p>Versión: <strong>{version}</strong></p>
        <p>Contedor que atende a petición:</p>
        <code>{hostname}</code>
        <p>Hora UTC: {datetime.now(timezone.utc).isoformat()}</p>
        <p>IP cliente observada: {request.remote_addr}</p>
      </div>
    </body>
    </html>
    """

@app.get("/health")
def health():
    return {"status": "ok"}, 200
