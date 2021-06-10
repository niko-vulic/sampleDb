import database.dbCommands
import database.dbInputOutput

USER_INPUT_INTRO = "Type 'exit' to quit or 'help' for a list of commands"
USER_INPUT_GOODBYE = 'EXIT command received. Terminating...'

HELP_COMMANDS_LIST = 'Available commands: exit, find, add'

EXIT = 'exit'
FIND = 'find'
ADD = 'add'
HELP = 'help'


class CommandInterpreter:
    def __init__(self, inMemoryDatabase, print_debug_statements=False):
        self.print_debug_statements = print_debug_statements
        self.inMemoryDatabase = inMemoryDatabase

        if print_debug_statements:
            print('DEBUG - CommandInterpreter - ON')

    # Main method to loop over user input
    def init_input_reader(self):
        print(USER_INPUT_INTRO)
        command = ''
        while command != EXIT:
            command = input("Command:")
            self.parse_command(command)

    # Command parse helper method
    def parse_command(self, input_string: str) -> None:
        if self.print_debug_statements:
            print('DEBUG - CommandInterpreter - inputString is:' + input_string)

        # Break condition
        if input_string == EXIT:
            print(USER_INPUT_GOODBYE)

        # HELP command
        elif input_string == HELP:
            print(HELP_COMMANDS_LIST)

        # FIND command takes an additional parameter, then performs a search and displays the result
        elif input_string == FIND:
            itemToFind = input('Find which item in database?:')
            item = database.dbCommands.findItem(itemToFind, self.inMemoryDatabase)
            if item:
                print('Found! ' + repr(item))
            else:
                print("Item '" + itemToFind + "' cannot be found!")

        # ADD command - adds or updates an existing item in DB
        elif input_string == ADD:
            itemToAdd = input('Add a new item. Format: name price type. ie: apple 2.99 fruit:')
            tempItem = generate_temporary_item_from_input(itemToAdd)
            #print('Temp item before DB add:' + repr(tempItem))

            # Only continue if the item was able to be parsed
            if tempItem:
                database_searched_item = database.dbCommands.findItem(tempItem.name, self.inMemoryDatabase)
                #print('Item searched from DB:' + repr(database_searched_item))

                if database_searched_item:
                    print('Item already exists in database!')
                else:
                    print('Adding item: ' + tempItem.name + ' to database')


def generate_temporary_item_from_input(input_string):
    split_item = str.split(input_string, ' ')
    if len(split_item) != 3:
        print('Invalid # of input parameters! ')
        return None

    item_name = split_item[0]
    item_type = split_item[2]
    item_price = 0
    try:
        item_price = int(split_item[1])
    except ValueError:
        print('Unable to parse price. Must be integer or float value')
        return None

    temp_db_item = database.dbInputOutput.DatabaseItem(item_name, item_price, item_type)
    return temp_db_item
