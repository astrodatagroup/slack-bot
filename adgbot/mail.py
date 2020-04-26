# -*- coding: utf-8 -*-

__all__ = ["send_message"]

import requests

from . import config


def send_message(url):
    message = config.get_email_template().replace("{slide_deck_url}", url)
    subject = "Today's group meeting"
    url = "https://api.mailgun.net/v3/{0}/messages".format(
        config.MAILGUN_JSON["domain"]
    )
    auth = ("api", config.MAILGUN_JSON["api_key"])
    data = {
        "from": config.MAILGUN_JSON["sender"],
        "to": config.SEND_TO_EMAIL,
        "subject": subject,
        "text": message,
    }
    return requests.post(url, auth=auth, data=data)
