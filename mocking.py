class UserClient:
    def __init__(self, *args, **kwargs):
        return None

    @property
    def api(self):
        return self

    @property
    def statuses(self):
        return self

    @property
    def update(self):
        return self

    def post(self, status=None):
        print(status)

