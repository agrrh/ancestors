class Database(object):
    """Database."""

    def __init__(self, host, port, user, pass_):
        self.handler = None

    def health(self):
        return self.handler.ping()
