from flask import Blueprint, request, Response, current_app
import json
from trade_executer_functions import send_signal_tradetron

forwarder = Blueprint('forwarder', __name__)

@forwarder.route('/"[redacted]"', methods=["POST"])
def forward_webhook():
    akey = request.args.get("[redacted]", default = "0", type = str)

    if akey in current_app.config["ALLOWED_KEYS"]:
        input_json = request.get_json()

        json_file = open("statefile", "r")
        data = json.load(json_file)
        json_file.close()

        current_p_state = data["p_state"]

        if input_json:
            if current_p_state != input_json["value"] and data["position_state"] == "1":
                exit_position_tradetron(current_p_state)
                data["position_state"] = "0" 

            elif current_p_state == input_json["value"] and data["position_state"] == "0":
                enter_position_tradetron(current_p_state)
                data["position_state"] = "1"

        else:
            input_string = request.get_data().decode("utf-8")
            direction = input_string[input_string.find(":") + 2]
            
            if direction == "-":
                direction += "1"

            if direction != current_p_state:
                send_signal_tradetron(direction)
            
                data["p_state"] = direction
                data["position_state"] = "1"
                
                json_file = open("statefile", "w")
                json_file.write(json.dumps(data))
                json_file.close()

        return Response(status = 200)

    else:
        return Response(status = 401)
