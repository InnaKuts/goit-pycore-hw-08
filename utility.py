import os
import pickle
from models import AddressBook, Record

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except (IndexError, KeyError, ValueError) as e:
            return f"Error: {e}"
    return inner

@input_error
def add_contact(args, book: AddressBook):
    name, phone, *_ = args
    record = book.find(name)
    message = "Contact updated."
    if record is None:
        record = Record(name)
        book.add_record(record)
        message = "Contact added."
    if phone:
        record.add_phone(phone)
    return message


@input_error
def change_phone(args, book: AddressBook):
    name, old_phone, new_phone = args
    record = book.find(name)
    if record:
        record.edit_phone(old_phone, new_phone)
        return "Phone number updated."
    return "Contact not found."


@input_error
def show_phone(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record:
        phones = ', '.join(phone.value for phone in record.phones)
        return f"{name}'s phone numbers: {phones}"
    return "Contact not found."


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    record = book.find(name)
    if record:
        record.add_birthday(birthday)
        return "Birthday added."
    return "Contact not found."


@input_error
def show_birthday(args, book: AddressBook):
    name = args[0]
    record = book.find(name)
    if record and record.birthday:
        return f"{name}'s birthday: {record.birthday.value.strftime('%d.%m.%Y')}"
    return "Birthday not found."


@input_error
def birthdays(args, book: AddressBook):
    days = int(args[0]) if len(args) > 0 else 7
    upcoming = book.get_upcoming_birthdays(days)
    result = []
    for record in upcoming:
        result.append(f"{record.name.value}: {record.birthday.value.strftime('%d.%m.%Y')}")
    return '\n'.join(result) if result else f"No birthdays in the next {days} days."


def show_all(book: AddressBook):
    result = []
    for record in book.data.values():
        result.append(str(record))
    return '\n'.join(result) if result else "No contacts in address book."


def parse_input(user_input):
    return user_input.strip().split(" ")

def save_data(book, filename="data/addressbook.pkl"):
    os.makedirs("data/", exist_ok=True)
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="data/addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()
