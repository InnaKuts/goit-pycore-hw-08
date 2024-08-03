from .field import Field

class Name(Field):
    def __init__(self, value):
        super().__init__(value)
        # Name specific validation or attributes can be added here

