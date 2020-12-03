# Bot Template: A simple sample echo bot to get started.
# Platform: MessengerX.io
# Author: @Abhishek Raj, Kumar Vaibhaw
# pip3 freeze > requirements.txt
from flask import request, jsonify, Response
from flask_api import FlaskAPI, status
import requests
import re
import json
import argparse
import os

from machaao import request_handler, send_message

from reply_methods import text_message_payload,quick_reply_payload,msg_with_quick_reply_payload,linked_button_payload,single_game_payload,five_game_payload

from get_games import update_game_data,top_5_games,single_game

# Wit Server accesss token
SERVER_ACCESS_TOKEN  = os.environ['WIT_API_KEY']


# Get your MESSENGERX_API_TOKEN from https://portal.messengerx.io
MESSENGERX_API_TOKEN = os.environ['MESSENGERX_API_KEY']

# For development use https://ganglia-dev.machaao.com
MESSENGERX_BASE_URL = os.environ['MESSENGERX_BASE_URL']

from wit import  Wit
def get_response(msg,SERVER_ACCESS_TOKEN):
    client=Wit(SERVER_ACCESS_TOKEN)
    response=client.message(msg)

    response=  (list(response['intents']))
    intent_confidence={}
    confidence=[0]
    for res in response:
        if(res['confidence']>=max(confidence)):
            intent_confidence = {}
            intent_confidence[res['name']]=res['confidence']
            confidence.append(res['confidence'])

    # retyrn format {'game_mode': 0.9968}

    return intent_confidence

# Updating database
# update_game_data()



app = FlaskAPI(__name__)



@app.route("/health")
def health_check():
    """
    Function to check, server running or not.
    """
    ret = {"Status": 200, "Msg": "Service is Up"}
    return jsonify(ret)


@app.route("/machaao/incoming", methods=["POST"])
def messageHandler():
    """
    Incoming message handler.
    """

    # Edit this function the way you want.

    incoming_data = request_handler(request)

    user_id = incoming_data["user_id"]

    message = incoming_data["messaging"]

    message = message[0]["message_data"]["text"]

    # Currently server set to echo.
    # Write your code here.

    response = get_response(message,SERVER_ACCESS_TOKEN)
    print("message ",message)
    # print(list(response.keys()), "   ->   game_mode" in (list(response.keys())))
    print(response)
    print()
    payload = ""

    # intent list = [greet, game_mode, latest_game, top_5_games, goodbye]

    if('greet' in list(response.keys())):
        payload=  msg_with_quick_reply_payload(user_id,"Hello, I am gameBot, would you like to play some games ?","yes","no")

    elif ("affirm" in list(response.keys())):
        payload = single_game_payload(user_id,single_game())

    elif ("deny" in list(response.keys())):
        payload=msg_with_quick_reply_payload(user_id,"Try our best top 5 games","yes","")

    elif ('game_mode' in list(response.keys())):
        payload = five_game_payload(user_id,top_5_games())

    elif ("lates_game" in list(response.keys())):
        payload=five_game_payload(user_id,top_5_games())

    elif('goodbye' in list(response.keys())):
        payload=msg_with_quick_reply_payload(user_id,"B,bye Have a nice day !","Start again","Exit")

    print(f"sending message -> using token: {MESSENGERX_API_TOKEN}, base_url: {MESSENGERX_BASE_URL}")


    # Read more about APIs here: https://ganglia.machaao.com/api-docs/#/
    # or here https://messengerx.readthedocs.io/en/latest/ or here
    # https://github.com/machaao/machaao-py
    response = send_message(MESSENGERX_API_TOKEN, MESSENGERX_BASE_URL, payload)

    output_payload = {
        "success": True,
        "message": response.text,
    }

    return Response(
        mimetype="application/json",
        response=json.dumps(output_payload),
        status=200,
    )


if __name__ == "__main__":
    _port = 5000
    print(f"starting at {_port}")
    app.run(host="0.0.0.0", port=_port)
