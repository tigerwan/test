import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

# slack_token = os.environ["SLACK_API_TOKEN"]
slack_token = "xoxb-3597524324-1204638407366-YOfKgyMgI41WTZsDQgj3U8dM"
client = WebClient(token=slack_token)

try:
  response = client.chat_postMessage(
    channel="copy-dest",
    text="a test"
  )
except SlackApiError as e:
  # You will get a SlackApiError if "ok" is False
  assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
