# twitch_notify notify streamer when they're streaming
# Copyright (C) 2021  Jan Poonthong
#
# twitch_notify is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# twitch_notify is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with twitch_notify.  If not, see <https://www.gnu.org/licenses/>.

#!/usr/bin/env python3

import argparse
import os
import sys

import requests
from dotenv import load_dotenv

load_dotenv('.env')
SECRET = os.environ['SECRET']
CLIENT_ID = os.environ['CLIENT_ID']


class Notify:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.twitch.tv/helix/streams?user_login={self.username}"
        self.auth = "https://id.twitch.tv/oauth2/token"
        self.client_id = CLIENT_ID
        self.secret = SECRET

    def get_token(self):
        auth_params = {'client_id': self.client_id,
                       'client_secret': self.secret,
                       'grant_type': 'client_credentials'
                       }
        aut_call = requests.post(url=self.auth, params=auth_params)
        token = aut_call.json()['access_token']
        head = {'Client-ID': self.client_id,
                'Authorization': "Bearer " + token
                }
        return head

    def check(self, head):
        try:
            content_json = requests.get(self.url, headers=head).json()["data"]

            if content_json:
                content_json = content_json[0]
                if content_json['type'] == 'live':
                    os.system("mpg123 " + "sound.mp3")
        except requests.exceptions.ConnectionError:
            self.check(head)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="""This bot can notify you with
                                     any twitch streamer with a sound.""")
    parser.add_argument('--user', type=str, help="username of twitch streamer")
    args = parser.parse_args()
    user_name = args.user
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    head_token = Notify(user_name).get_token()
    while True:
        Notify(user_name).check(head_token)
