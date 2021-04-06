#!/usr/bin/env python3

import requests
import os
import sys
import argparse
from dotenv import load_dotenv

load_dotenv('.env')
SECRET = os.environ['SECRET']
CLIENT_ID = os.environ['CLIENT_ID']

class Notifly:
    def __init__(self, username):
        self.username = username
        self.url = f"https://api.twitch.tv/helix/streams?user_login={self.username}"
        self.auth = "https://id.twitch.tv/oauth2/token"
        self.client_id = CLIENT_ID
        self.secret = SECRET

    def check(self):
        try:
            auth_params = {'client_id': self.client_id,
                           'client_secret': self.secret,
                           'grant_type': 'client_credentials'
                           }
            aut_call = requests.post(url=self.auth, params=auth_params)
            token = aut_call.json()['access_token']
            head = {'Client-ID': self.client_id,
                    'Authorization':  "Bearer " + token
                    }
            content_json = requests.get(self.url, headers=head).json()["data"]

            if content_json:
                content_json = content_json[0]
                if content_json['type'] == 'live':
                    os.system("mpg123 " + "sound.mp3")
                    return True
                else:
                    return False
            else:
                return False
        except requests.exceptions.ConnectionError:
            self.check()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="This bot can notify you with any twitch streamer with a sound.")
    parser.add_argument('--user', type=str, help="username of twitch streamer")
    args = parser.parse_args()
    username = args.user
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit()

    while True:
        print(Notifly(username).check())
