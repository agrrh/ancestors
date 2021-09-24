class Account(object):
    """Account."""

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

        self.email = None
        # self.password = None
