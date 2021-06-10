import database.dbCommands

USER_INPUT_INTRO = "Type 'exit' to quit or 'help' for a list of commands"

EXIT = 'exit'
FIND = 'find'
HELP = ['help', 'h']

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

        if input_string == EXIT:
            print('EXIT command received. Terminating...')
        elif input_string == FIND:
            itemToFind = input('Find which item in database?:')
            item = database.dbCommands.findItem(itemToFind, self.inMemoryDatabase)
            print(item)