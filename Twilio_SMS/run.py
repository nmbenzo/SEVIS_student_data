from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import Twilio_SMS.sms_templates as template
import logging


logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_regular_response(response=template.General_ISSS_response):
    """Respond to an incoming message with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    # Add a message
    resp.message(response)

    return str(resp)


@app.route("/MessageStatus", methods=['POST'])
def incoming_sms():
    message_sid = request.values.get('MessageSid', None)
    message_status = request.values.get('MessageStatus', None)
    logging.info(f'SID: {message_sid}, Status: {message_status}')
    return ('', 204)


if __name__ == "__main__":
    app.run(debug=True)