# -*- coding: utf-8 -*-

from . import google, slack


def main() -> None:
    new_file = google.create_new_deck()
    slack.post_message(
        "Hello! I created a new slide deck for this week's group meeting. "
        "Add your slide here: {0}".format(new_file["webViewLink"])
    )
