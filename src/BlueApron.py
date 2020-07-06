
# **# In-memory datastore**

#
# SET key,value
#
# GET key
#
# UNSET key  ... remove entry from database
#
# COUNT value
#
# Assumptions:
# - Every item has a unique key
# - The value contains a single field, integer or string.
# - Input from console
# - The key and value on the set statement are comma delimited without whitespace.


database = {}

def set_command (key, value):

    if key is None:
        print("\n! The SET command must have a key and value separated by a command: key, value!\n")
        return
    if value is None:
        print("\n ! A key was found on the SET command, but there was no value. Enter both key, value!\n")

    database[key] = value

def get_command(key):

    if key is None:
        print("\n! The GET command must have a key and none was provided!\n")
        return

    if key in database.keys():
        return database[key]
    else:
        print("\n !key of {} not found!\n".format(key))
        return None

def unset_command(key):

    if key is None:
        print("\n! The UNSET command must have a key and none was provided!\n")
        return

    if key in database.keys():
        del database[key]
    else:
        print("\n !key of {} not found!\n".format(key))
        return None

def count_command(value):

    if key is None:
        print("\n! The COUNT command must have a value and none was provided!\n")
        return

    count = 0
    for db_value in database.values():
        if value == db_value: count += 1

    return count


if __name__ == '__main__':

    print("In memory data store. Blue Apron coding exercise.")
    print("Here are the available commands:")
    print("1. SET key value     # To add a new record.")
    print("2. GET key           # To retrive the value for a key.")
    print("3. UNSET key         # To remove an entry from the database.")
    print("4. COUNT value       # To count the occurences of a value in the database.")
    print("5. QUIT              # To exit this program.")
    print("")

    command = input("Enter a command > ")
    while command.upper() != "QUIT":
        print("command = {}".format(command))

        # Parse the command verb by splitting on space
        tokens = command.split(' ')
        command = tokens[0].upper() if len(tokens) > 0 else None

        # Parse the parameters by splitting the second token on comma
        parameters = tokens[1].split(',') if len(tokens) > 1 else None
        key = parameters[0] if parameters is not None else None
        value = parameters[1] if parameters is not None and len(parameters) > 1 is not None else None
        
        if command == "SET":
            set_command(key, value)
        elif command == "GET":
            the_value = get_command(key)
            if the_value is not None: print("\n The value associated with {} is {}.\n".format(key, the_value))
        elif command == "UNSET":
            unset_command(key)
        elif command == "COUNT":
            count = count_command(key) # The command syntax does not have a key, but the value is parsed into the key variable
            if count is not  None:
                plural = "times" if count != 1 else "time"
                print("\n The value of {} occurs {} {}.\n".format(key, count, plural))
        else:
            print("\nInvalid command. Use SET, GET, UNSET, COMMAND, or QUIT\n")

        command = input("Enter a command > ")
