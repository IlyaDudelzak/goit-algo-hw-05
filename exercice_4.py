contacts = {}
debug = False

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter the argument for the command"
        except KeyError:
          print(KeyError)
        except IndexError:
          print(IndexError)

    return inner

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args):
    name, phone = args
    if(name.casefold() in contacts):
      raise ValueError
    contacts[name.casefold()] = phone
    return "Contact added."

@input_error
def change_contact(args):
    name, phone = args
    if(name not in contacts):
      raise ValueError
    contacts[name.casefold()] = phone
    return "Contact changed."

def get_phone(args):
  try:
    if args[0].casefold() in contacts.keys():
      return contacts[args[0].casefold()]
    else:
      return 1
  except Exception as e:
    return -1
    if(debug):
      print(e)

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
            r = change_contact(args)
            if(r==0):
              print("Success!")
            elif(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Wrong args!")

        elif command == "phone":
            r = get_phone(args)
            if(r==1):
              print("Contact of " + args[0] + " doesn`t exist.")
            elif(r==-1):
              print("Wrong args!")
            else:
              print(r)

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
