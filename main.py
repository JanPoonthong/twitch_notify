import requests
import os
import time


class Notifly:
    def __init__(self):
        self.url = "https://api.twitch.tv/helix/streams?user_login=strager"
        self.auth = "https://id.twitch.tv/oauth2/token"
        self.client_id = ""
        self.secret = ""

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
                    print("https://www.twitch.tv/strager")
                    return True
                else:
                    return False
            else:
                return False
        except ConnectionError:
            self.check()


if __name__ == "__main__":
    while True:
        print(Notifly().check())
        time.sleep(1)
