import threading
from flask import Flask, json, request
import requests
import replicate
import os
import time

# Slack OAuth Access Token
slack_token = "<your-bot-user-oauth-token>"
response_url = "<your-incoming-webhook-url>"

os.environ['REPLICATE_API_TOKEN'] = "<your-replicate-api=token>"
model = replicate.models.get("borisdayma/dalle-mini")

# Initialize the Flask object which will be used to handle HTTP requests
# from Slack
app = Flask(__name__)


@app.route("/galle", methods=["POST"])
def dalle_handler():

    data = request.form.get("text")
    channel = request.form.get("channel_id"),

    # starting a new thread for doing the actual processing
    x = threading.Thread(
        target=sub_dalle,
        args=[data, channel])
    x.start()

    return "Generating image.... please wait (can take  ~30 sec)"


def sub_dalle(data, channel):

    start = time.time()
    my_dict = model.predict(prompt=data, n_predictions=1)

    time_taken = time.time() - start
    url = my_dict[0]['image']

    text = f"{time_taken} sec taken to get {url}"

    payload = {"token": slack_token,
               "channel": channel,
               "text": text}

    requests.post(response_url,
                  json.dumps(payload))


# Run on local port 3000
if __name__ == "__main__":
    app.run(port=3000, debug=True)
