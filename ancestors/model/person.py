class Person(object):
    """docstring for Person."""

    def __init__(self, **kwargs):
        self.id = kwargs.get("id")

        self.name = None

        self.birth = None
        self.death = None

        self.father = None
        self.mother = None

        self.facts = []
