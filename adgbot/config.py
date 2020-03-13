# -*- coding: utf-8 -*-

__all__ = [
    "PRESENTATION_TITLE",
    "SHARED_DRIVE_NAME",
    "TEMPLATE_NAME",
    "SHARE_WITH_EMAIL",
    "get_google_json",
    "get_slack_json",
]

import os
import json


def get_google_json():
    if "GOOGLE_INFO" in os.environ:
        return json.loads(os.environ["GOOGLE_INFO"])
    with open("secrets/google.json", "r") as f:
        return json.load(f)


def get_slack_json():
    if "SLACK_INFO" in os.environ:
        return json.loads(os.environ["SLACK_INFO"])
    with open("secrets/slack.json", "r") as f:
        return json.load(f)


GOOGLE_JSON = get_google_json()
SLACK_JSON = get_slack_json()

PRESENTATION_TITLE = os.environ.get(
    "PRESENTATION_TITLE", "Astro Data Group Meeting"
)
SHARED_DRIVE_NAME = os.environ.get(
    "SHARED_DRIVE_NAME", "Astronomical Data Group"
)
TEMPLATE_NAME = os.environ.get("TEMPLATE_NAME", "__template__")
SHARE_WITH_EMAIL = os.environ.get(
    "SHARE_WITH_EMAIL", "astro-data-group@googlegroups.com"
)

