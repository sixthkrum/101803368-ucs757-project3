from flask import Flask

app = Flask(__name__)
app.secret_key = "[redacted]"
app.config["ALLOWED_KEYS"] = ["[redacted]"]
app.config["REMOTE_API_KEY_TRADETRON"] = "[redacted]"

#blueprints
from public_routes import forwarder 
app.register_blueprint(forwarder)
