contacts = {}
debug = False

class ContactError(Exception):
   pass

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
          return "Wrong args!"
        except (KeyError,IndexError,ContactError) as e:
          return str(e)

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args):
    name, phone = args
    if(name.casefold() in contacts):
      raise ContactError("Contact already registried")
    contacts[name.casefold()] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    if(name not in contacts):
      raise ContactError("Contact isn`t registried")
    contacts[name.casefold()] = phone
    return "Contact changed."

def get_phone(args):
    if args[0].casefold() in contacts.keys():
      return contacts[args[0].casefold()]
    else:
      raise ContactError("Contact isn`t registried")

def get_all(args):
  try:
    contacts_ = []
    for i in contacts:
      contacts_.append(i + ": " + contacts[i])
    return contacts_
  except Exception as e:

    if(debug):
      print(e)

def main():
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
            print(add_contact(args))

        elif command == "change":
            print(change_contact(args))

        elif command == "phone":
            print(get_phone(args))

        elif command == "all":
            r = get_all(args)
            if(len(r) == 0):
              print("There are no contacts registried.")
            else:
              for i in r:
                print(i)

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
