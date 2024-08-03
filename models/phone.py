from .field import Field

class Phone(Field):
    def __init__(self, value):
        if self.validate_phone(value):
            super().__init__(value)
        else:
            raise ValueError("Invalid phone number format")

    def validate_phone(self, phone):
        return phone.isdigit() and len(phone) == 10
