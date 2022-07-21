## Setup & Installation

* Install ngrok: https://dashboard.ngrok.com/get-started/setup
* Run
```
ngrok http 3000
```
This exposes your local flask server using a randomly assigned URL that you get from the command. This will be of the form
https://<xxx>.ngrok.io. Note this URL will change everytime you restart ngrok.

* Create a new Slack App: https://api.slack.com/apps
  * Click "Create New App", choose "From scratch" option
  * Provide an App Name, Select a workspace
  * Add Features & Functionality
    * Slash Commands: 
      * Command: /galle
      * Request URL: provide the ngrok URL you got above
      * Short Description: Generates an image from a text prompt using Dall-E
      * Usage Hint: "<text prompt>"
    * OAuth & Permissions
      * The Bot User OAuth Token you see here is the slack token you will use in your code
      * Scopes: Enable the following bot token scopes: `chat:write`, `chat:write_customize`, `chat:write.public`, `commands`, `incoming-webhook` 
    * Activate Incoming Webhooks
      * The webhook URL you see here is what is provided as the response URL in the code
  * Install your app:
    * Install to Workspace: specify channels that the bot can post to
  * Manage Distribution: To install app in other workspaces


## Replicate API
Although you can run the DALL-E mini and similar models locally, they take a significant amount of compute and a GPU
to run in a reasonable amount of time. For this implementation, I opted to get the images using the Replicate API. This 
requires a "Hobby" subscription ($10/month). The API token is provided in the code.

There are several models available via Replicate and the code allows you to switch using the following dict:
```commandline
model_dict = {"borisdayma": "borisdayma/dalle-mini",
              "kuprel": "kuprel/min-dalle",
              "mehdidc": "mehdidc/feed_forward_vqgan_clip"}
```

The first two take ~ 25 sec, the third one is significantly faster at ~ 3 sec.

## Run flask server

* Create a conda environment: 
```commandline
conda create -n "dalle" python=3.8
pip install flask replicate 
```

* Run flask server to serve generated images to slack workspace
```commandline
python dalle_slackbot.py
```

### Run on Google Cloud
* Create a basic f1-micro (~$5/month) instance
* Installation
```
# Get ngrok & other tools
curl https://bin.equinox.io/c/4VmDzA7iaHb/ngrok-stable-linux-amd64.zip -o ngrok-stable-linux-amd64.zip
sudo apt-get install unzip tmux git
unzip ngrok-stable-linux-amd64.zip
```
* Run ngrok in a tmux session
```
tmux
./ngrok authtoken <token>
```
* Run flask server in a separate tmux session
```
tmux
git clone https://github.com/sanzgiri/dalle_slackbot.git
pip3 install flask replicate packaging
cd dalle_slackbot
python3 dalle_slackbot.py
```
