# Notify twitch stream

This bot can notify you with any twitch streamer with a sound.

## Requirements

## Linux

Instructions:

1.  Download mpg123:

        $ sudo apt install mpg123

2.  Install requests:

        $ pip3 install requests

3.  Install dotenv:

        $ pip3 install python-dotenv

4.  Don't create `.env-example`. Create a `.env` file to store credentials `CLIENT_ID`
    and `SECRET`.

5.  Run:

        $  python3 main.py <strager> or ./main.py <strager>
