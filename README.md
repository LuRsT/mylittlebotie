# mylittlebotie

The simplest possible twitter bot

## How to use?

- Create a twitter account
- Add an app
- Add access token to app
- Fill in necessary environment variables:
    - TWITTER_CONSUMER_KEY
    - TWITTER_CONSUMER_SECRET
    - TWITTER_ACCESS_TOKEN
    - TWITTER_ACCESS_TOKEN_SECRET
- Create a virtual environment (Optional)
- Install requirements
    - `pip install -r requirements.txt`
- Run it: `python main.py`
- Check twitter account

## How to make it bot-like

Add this line to your crontab:

    0 * * * * python main.py


## Known issues

- The client raises an exception if we send the same status update, which with
the current implementation will happen very quickly.
