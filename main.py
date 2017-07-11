import random

from client import CLIENT


if __name__ == '__main__':
    die_result = random.randint(1,6)
    status = 'I just threw a die and the result was {}'.format(die_result)
    response = CLIENT.api.statuses.update.post(status=status)
