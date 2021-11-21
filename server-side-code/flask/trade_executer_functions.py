import requests
from flask import current_app

def send_signal_tradetron(state):
    requests.post('https://api.tradetron.tech/api?', data = {"auth-token" : current_app.config["REMOTE_API_KEY_TRADETRON"], "key" : "nfott", "value" : state}, verify = True, timeout = 2)
