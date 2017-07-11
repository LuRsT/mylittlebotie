import os
import random

from birdy.twitter import UserClient


CONSUMER_KEY = os.environ.get('TWITTER_CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('TWITTER_CONSUMER_SECRET')
ACCESS_TOKEN = os.environ.get('TWITTER_ACCESS_TOKEN')
ACCESS_TOKEN_SECRET = os.environ.get('TWITTER_ACCESS_TOKEN_SECRET')


def send_twitt(status):
    client = UserClient(
        CONSUMER_KEY,
        CONSUMER_SECRET,
        ACCESS_TOKEN,
        ACCESS_TOKEN_SECRET,
    )
    client.api.statuses.update.post(status=status)
    print("You just sent a twitt! Good job!")


if __name__ == '__main__':
    die_result = random.randint(1,6)
    status = 'I just threw a die and the result was {}'.format(die_result)
    send_twitt(status)
