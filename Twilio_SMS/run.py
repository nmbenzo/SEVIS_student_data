from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Twilio_SMS.sms_templates as template


app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])

def sms_regular_response(response=template.General_ISSS_response):
    """Respond to an incoming message with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(response)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)