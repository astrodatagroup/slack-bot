# -*- coding: utf-8 -*-

__all__ = ["post_message"]

import requests

from . import config


def post_message(message):
    secrets = config.SLACK_JSON
    r = requests.post(secrets["webhook_url"], json=dict(text=message))
    r.raise_for_status()
