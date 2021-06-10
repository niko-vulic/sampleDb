import database.dbCommands

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
            #print('DEBUG - CommandInterpreter - inputString is:' + input_string)

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