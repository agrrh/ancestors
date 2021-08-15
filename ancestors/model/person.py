class Person(object):
    """Person."""

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

        self.names = []

        self.birth = None
        self.death = None

        self.relatives = []

        self.facts = []
