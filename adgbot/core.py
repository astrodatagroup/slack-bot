# -*- coding: utf-8 -*-

from . import google, slack, mail, config


def main(*args, **kwargs) -> None:
    new_file = google.create_new_deck()
    message = """
THIS IS A TEST - IGNORE ME!

Hello! I created a new slide deck for this week's group meeting.

Add your slide here: {0}

Join the meeting via Zoom: {1}
""".strip().format(
        new_file["webViewLink"], config.ZOOM_LINK
    )
    slack.post_message(message)
    mail.send_message(new_file["webViewLink"])
    return {
        "statusCode": "200",
        "body": '{"message": "success"}',
        "headers": {"Content-Type": "application/json"},
    }
