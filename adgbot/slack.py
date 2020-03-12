# -*- coding: utf-8 -*-

__all__ = ["post_message"]

import requests

from . import config


def post_message(message):
    secrets = config.get_slack_json()
    r = requests.post(
        secrets["webhook_url"], json=dict(text="[THIS IS A TEST]: " + message)
    )
    r.raise_for_status()
