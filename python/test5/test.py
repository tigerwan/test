import slack
from urllib.error import URLError, HTTPError
def slacker_chat_bot():
    """Post message to Slack and log result."""
    print("sending message...")
    channel = '#argos-notifications'
    # channel = 'C012Y6ZJZSB'
    slack_message = {
                "channel": channel,
                "attachments": [
                    {
                       "fallback": "Title - Daniel Test",
                       "color": "#36a64f", "title": "Test",
                       "text": "daniel Test text"
                    }
                    ]
                }
    print(slack_message)
    client = slack.WebClient(token='xoxb-3597524324-1204638407366-YOfKgyMgI41WTZsDQgj3U8dM')  # TODO please enter here token value
    print(channel)
    try:
        client.chat_postMessage(channel=channel,
                                attachments=slack_message['attachments'])
        print("Message posted")
    except HTTPError as e:
        print("Request failed : %d %s", e.code, e.reason)
    except URLError as e:
        print("Server connection failed: %s", e.reason)


def lambd_handler(event, context):
    slacker_chat_bot()

if __name__ == '__main__':
    slacker_chat_bot()
