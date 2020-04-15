import requests
import json
import slackweb
from config import config

slack = slackweb.Slack(url=config["slack_info"]["in_webhook_url"])

def slack_notify(text_="", list_None):
    slack.notify(text=text_)
    for element in list_:
        #タイトル
        slack.notify(text=element[0])
        #url
        slack.notify(text=element[1])

webhook_url = "https://hooks.slack.com/services/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"
#"https://hooks.slack.com/services/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"

text = "PythonでSlackにメッセージを送る"

requests.post(webhook_url, data = json.dumps({
    "text": text
}))
