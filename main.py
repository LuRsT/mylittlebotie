# from birdy.twitter import UserClient
from mocking import UserClient

CONSUMER_KEY = ''
CONSUMER_SECRET = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

client = UserClient(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET,
)

response = client.api.statuses.update.post(status='Hello World!')
