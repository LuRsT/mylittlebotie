import os
import requests

from birdy.twitter import UserClient


def send_twitt(status):
    client = UserClient(
        os.environ['TWITTER_CONSUMER_KEY'],
        os.environ['TWITTER_CONSUMER_SECRET'],
        os.environ['TWITTER_ACCESS_TOKEN'],
        os.environ['TWITTER_ACCESS_TOKEN_SECRET'],
    )
    try:
        client.api.statuses.update.post(status=status)
    except:
        print("Sorry, something has gone wrong...try again?")
    else:
        print("You just sent a twitt! Good job!")


if __name__ == '__main__':
    request = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    status = 'Random wiki article: {}'.format(request.url)
    send_twitt(status)
