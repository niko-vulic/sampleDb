import config.configHandler
import database.dbInputOutput


class DbInterface:
    def __init__(self, print_debug_statements=False):

        # Initialize the config first
        self.dbConfig = config.configHandler.DatabaseConfiguration(print_debug_statements)
        self.version = self.dbConfig.codeVersion
        if print_debug_statements:
            print('Database Config Initialized')
            print('Database Code Version : ' + str(self.version))
            print('DatabaseConfig:' + str(self.dbConfig))

        # Initialize the In-Memory Database
        self.inMemoryDatabase = database.dbInputOutput.read_db(self.dbConfig, print_debug_statements)

        # Read user commands
        print('--- Database Project V:' + str(self.version) + ' ready ---')
        userCommand = ''
        while userCommand != 'exit':
            userCommand = input("Command:")

        print('--- Database Project V:' + str(self.version) + ' terminated ---')
