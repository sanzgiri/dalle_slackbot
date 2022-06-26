## Setup & Installation

* Install ngrok: https://dashboard.ngrok.com/get-started/setup and run
```
ngrok http 3000
```
This exposes your local flask server using a randomly assigned URL that you get from the command. This will be of the form
https://<xxx>.ngrok.io. Note this will change everytime you restart ngrok.

* Create a new Slack App: https://api.slack.com/apps
  * From scratch
  * Give it an App Name, select a workspace
  * Add Features & Functionality
    * Slash Commands: 
      * Command: /galle
      * Request URL: ngrok URL you got above
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


## Mini Dall-E API
The images are generated using the DALL-E mini model: https://github.com/borisdayma/dalle-mini. 
Although this can be run locally, it takes a significant amount of compute. For this implementation,
I opted to get the images using an API hosted at https://replicate.com/borisdayma/dalle-mini. This requires 
a "Hobby" subscription ($10/month). The API token has to be provided in the code.


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
