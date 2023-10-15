phones = {}
commands = [
    "new_contact", "show_contacts"
]
while True:
    command = input(f"Pick an option: {commands}: ")
    while command not in commands:
        print("Unknown command, try again: \n")
        command = input(f"Pick an option: {commands}: ")
    if command == "new_contact":
        name = input("Type full name of user: ")
        phone_number = input("Type users phone number: ")
        phones[name] = phone_number
    elif command == "show_contacts":
        print("This is your current dictionary: \n")
        for name, phone in phones.items():
            print(name, phone)
    command = input("Do you want to continue? (Y/N): ")
    if command == "N":
        break
