import random
from flask import Flask, request
from pymessenger.bot import Bot

app = Flask(__name__)
ACCESS_TOKEN = 'EAAEGVoPSYz0BAENjbvjmTolsduJUgZAXpU99f2cKmwLDn5OStREVWnxW8ZCCJ5cLBxlMl6ietI1kgdlLp3BJaqaW4hKecsSxHaECemEOIRYXOtKnRDZAv0OegLE6DHZAbbnxZBxsBz2yQltm8JxcFJWd9J4L3AKlz6w5qTxQLX9tuSdqwlyZBL'
VERIFY_TOKEN = 'VERIFY_TOKEN'
bot = Bot(ACCESS_TOKEN)

@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       for event in output['entry']:
          messaging = event['messaging']
          for message in messaging:
            if message.get('message'):
                if message['message'].get('text'):
                    response_sent_text = get_message()
                    send_message(recipient_id, response_sent_text)
    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'

def get_message():
    sample_responses = ["Your server is up and running!",
    "No malicious activity detected so far.",
    "Potentail threat detected!"]
    return random.choice(sample_responses)


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"

if __name__ == "__main__":
    app.run()
