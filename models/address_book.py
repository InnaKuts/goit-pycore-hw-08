from collections import UserDict
from datetime import datetime, timedelta

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
    
    def get_upcoming_birthdays(self, days=7):
        current_date = datetime.now()
        upcoming_birthdays = []
        for record in self.data.values():
            if record.birthday:
                birthday_this_year = record.birthday.value.replace(year=current_date.year)
                if current_date <= birthday_this_year <= current_date + timedelta(days=days):
                    upcoming_birthdays.append(record)
        return upcoming_birthdays