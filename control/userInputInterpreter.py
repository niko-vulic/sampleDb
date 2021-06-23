import logging

import database.dbCommands
import database.dbInputOutput
import config.dbConstants as dbConst

USER_INPUT_INTRO = "Type 'exit' to quit or 'help' for a list of commands"
USER_INPUT_GOODBYE = 'EXIT command received. Terminating...'
HELP_COMMANDS_LIST = 'Available commands: exit, find, add, list, delete'

HELP = 'help'
EXIT = 'exit'

FIND = 'find'
ADD = 'add'
LIST = 'list'
DELETE = 'delete'
CONFIG = 'config'

ANSWER_NO = 'n'
ANSWER_YES = 'y'


class CommandInterpreter:
    def __init__(self, inMemoryDatabase, db_config, print_debug_statements=False):
        self.print_debug_statements = print_debug_statements
        self.inMemoryDatabase = inMemoryDatabase
        self.db_config = db_config

        self.logger = logging.getLogger(dbConst.USER_COMMANDS)
        self.logger.setLevel(db_config.logLevel[dbConst.USER_COMMANDS])

        self.logger.debug('User command interpreter ONLINE')

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

        # EXIT command - Break condition
        if input_string == EXIT:
            print(USER_INPUT_GOODBYE)

        # HELP command
        elif input_string == HELP:
            print(HELP_COMMANDS_LIST)

        # FIND command takes an additional parameter, then performs a search and displays the result
        elif input_string == FIND:
            item_name = input('Find which item in database?:')
            item = database.dbCommands.find_item(item_name, self.inMemoryDatabase)
            if item:
                print('Found! ' + repr(item))
            else:
                print("Item '" + itemToFind + "' cannot be found!")

        # ADD + UPDATE command - adds or updates an existing item in DB
        elif input_string == ADD:
            item_to_add = input('Add a new item. Format: name price type. ie: apple 2.99 fruit:')
            temp_item = generate_temporary_item_from_input(item_to_add)
            # print('Temp item before DB add:' + repr(tempItem))

            # Only continue if the item was able to be parsed
            if temp_item:
                database_searched_item = database.dbCommands.find_item(temp_item.name, self.inMemoryDatabase)
                # print('Item searched from DB:' + repr(database_searched_item))

                if database_searched_item:
                    update_item_answer = input('Item already exists in database! Update with new price and type? y/n')

                    if parse_yes_no_answer(update_item_answer):
                        database.dbCommands.update_item(temp_item, self.inMemoryDatabase)
                        print('Item: ' + temp_item.name + ' has been updated')
                    else:
                        print('Item: ' + temp_item.name + ' has not been updated')
                else:
                    print('Adding item: ' + temp_item.name + ' to database')
                    database.dbCommands.add_item(temp_item, self.inMemoryDatabase)

        # LIST command - list all items from the DB using their string representation
        elif input_string == LIST:
            for database_item in self.inMemoryDatabase:
                print(repr(database_item))

        # DELETE command - remove an item from DB
        elif input_string == DELETE:
            item_to_delete_name = input('Delete which item in database?:')
            if database.dbCommands.delete_item(item_to_delete_name, self.inMemoryDatabase):
                print('Item: ' + item_to_delete_name + ' has been deleted!')
            else:
                print('Item: ' + item_to_delete_name + ' does not exist in database, cannot be deleted!')

        # CONFIG command - update config params
        elif input_string == CONFIG:
            print('Valid loggers:' + str(self.db_config.logLevel.keys()))
            print('Valid log levels:' + str(dbConst.VALID_LOG_LEVELS))
            logger_name_to_update = input('Logger name to update:')
            logger_level_to_udpate = input('New logger level:')
            print(self.db_config.update_log_level(logger_name_to_update, logger_level_to_udpate))



def parse_yes_no_answer(input_string) -> bool:
    """Force user to input either 'y' or 'n'"""
    while not (input_string == ANSWER_NO or input_string == ANSWER_YES):
        input_string = input('Invalid answer. y/n?')

    if input_string == ANSWER_YES:
        return True
    else:
        return False


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
