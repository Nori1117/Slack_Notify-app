import slackweb
from config import config

slack = slackweb.Slack(url=config['slack_info']['in_webhook_url'])
slack.notify(text="test")
