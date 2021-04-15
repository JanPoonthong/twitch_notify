# Notify twitch stream

This bot can notify you with any twitch streamer with a sound.

## Requirements

## Linux

Instructions:

1. Download mpg123:

        $ sudo apt install mpg123

2. Install dotenv:

        pip3 install python-dotenv

3. Create a `.env` file to store credentials `CLIENT_ID` and `SECRET`. Don't
   create `.env-example`

4. Run:

        $  python3 main.py --user <strager> or ./main.py --user <strager>
