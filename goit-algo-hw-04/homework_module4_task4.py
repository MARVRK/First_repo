def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact (args, contacts):
    try:
        name, phone = args   
        if name in contacts:
                contacts[name]=phone
                return "Contact Updated"     
        else:
                return "Name doesn't match or not exist!"
    except ValueError :
        return "not enough values to unpack (expected 2, got 1)"
   
def show_phone (args, contacts):
    key = args[0] if args else None
    if key in contacts:
        phone_number = contacts[key]
        return f"Phone number for {key}: {phone_number}"
    else:
        return "there is now key in then list!"
    
def show_all(contacts):
    list_of_contacts=[]
    if contacts:
        list_of_contacts.append([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
        return list_of_contacts
    else:
        return "List of contacts is empty."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args,contacts))
        elif command == "all":
            print(show_all(contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "test":
            print(test(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    