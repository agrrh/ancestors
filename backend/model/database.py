class Database(object):
    """Database."""

    def __init__(self, address, port, username, password):
        self.handler = None

    def health(self):
        return {"status": True}
