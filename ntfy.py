import requests
import json

webhook_url = "https://hooks.slack.com/services/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"
#"https://hooks.slack.com/services/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"

text = "PythonでSlackにメッセージを送る"

requests.post(webhook_url, data = json.dumps({
    "text": text
}))
