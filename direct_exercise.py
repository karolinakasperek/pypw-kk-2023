phones = {}

while True:
    command = input("Pick an option: new_contact, show_contacts: ")
    if command == "new_contact":
        name = input("Type full name of user: ")
        phone_number = input("Type users phone number: ")
        phones[name] = phone_number
    elif command == "show_contacts":
        print("This is your current dictionary: \n")
        for name, phone in phones.items():
            print(name, phone)
    else:
        print("Unknown command")

    command = input("Do you want to continue? (Y/N): ")
    if command == "N":
        break
