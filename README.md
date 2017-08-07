# mylittlebotie

The simplest possible twitter bot.

It twittes a random Wikipedia page every time you run the script.

Example of this script in use: https://twitter.com/mylittlebotie


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

Note: You need to pass the env vars somehow to the environment runing the
script.


## Known issues

- The client raises an exception if we send the same status update, which with
the current implementation will happen very quickly.


## Tips and tricks

To easily run the script without having to set the twitter keys all the time,
you can create a `keys.sh` file which will store them (this is NOT safe!) and
then you run `source keys.sh` and now you can run `python main.py` without an
issue.

Example `keys.sh` file:

    export TWITTER_CONSUMER_KEY="<KEY>"
    export TWITTER_CONSUMER_SECRET="<KEY>"
    export TWITTER_ACCESS_TOKEN="<KEY>"
    export TWITTER_ACCESS_TOKEN_SECRET="<KEY>"

Note: `keys.sh` is already in `.gitignore`
