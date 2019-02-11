from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from Twilio_SMS.sms_templates import *


app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])

def sms_regular_response(response=General_ISSS_response):
    """Respond to an incoming message with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(response)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)