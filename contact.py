#task 4
from decorators import input_error


@input_error
def add_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise ValueError("2 arguments (name & phone) are required.")
    name, phone = args
    contacts[name] = phone
    return "Provided contact is added."


@input_error
def change_contact(args: list, contacts: dict) -> str:
    if len(args) != 2:
        raise ValueError("2 arguments (name & phone) are required.")
    name, phone = args
    if name not in contacts:
        raise KeyError("Provided contact does not exist.")
    contacts[name] = phone
    return "Contact is updated."


@input_error
def get_contact(args: list, contacts: dict) -> str:
    if len(args) != 1:
        raise ValueError("At least 1 argument (name) is required.")
    name = args[0]
    if name not in contacts:
        raise KeyError("Provided contact does not exist.")
    return contacts[name]


@input_error
def get_all_contacts(contacts: dict) -> str:
    if not contacts:
        return "Contacts are empty"
    else:
        output = "Contacts:"
        for name, phone in contacts.items():
            output += f"\n{name}: {phone}"
        return output