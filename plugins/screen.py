from neb.plugins import Plugin

import base64


class Base64Plugin(Plugin):
    """Control the Kodi screens
    screen play <url> : Plays the video.
    """

    name="screen"

    def cmd_play(self, event, *args):
        return base64.b64encode(event["content"]["body"][12:])
