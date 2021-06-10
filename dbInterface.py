import config.configHandler
import database.dbInputOutput
import control.userInputInterpreter


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
        self.parsedDatabase = database.dbInputOutput.read_db(self.dbConfig, print_debug_statements)
        self.inMemoryDatabase = database.dbInputOutput.generate_object_db_representation(self.dbConfig, self.parsedDatabase, print_debug_statements)

        print('--- Database Project V:' + str(self.version) + ' ready ---')
        # Read user commands
        self.inputInterpreter = control.userInputInterpreter.CommandInterpreter(self.inMemoryDatabase, print_debug_statements)
        self.inputInterpreter.init_input_reader()
        print('--- Database Project V:' + str(self.version) + ' terminated ---')
