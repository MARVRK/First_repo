def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "index out of range"
        except KeyError:
            return "No such name found in contacts"
    return inner

@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error
def change_contact (args, contacts):    
    name, phone = args   
    if name in contacts:
        contacts[name]=phone
        return "Contact Updated"     
    else:
        return "Name doesn't match or not exist!"

@input_error
def show_phone (args, contacts): 
    key = args[0]
    phone_number = contacts.get(key)
    if phone_number:
        return f"Phone number for {key}: {phone_number}"
    else:
        raise KeyError
        
@input_error
def show_all(contacts):
    list_of_contacts=[]
    if contacts:
        list_of_contacts.append([f"{name}: {phone_number}" for name, phone_number in contacts.items()])
        return list_of_contacts
    else:
        return "list is empty"
    
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
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

    