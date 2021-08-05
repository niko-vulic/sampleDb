import config.configHandler
import database.dbInputOutput as dbIo
import control.userInputInterpreter


class DbInterface:
    def __init__(self, print_debug_statements=False):

        # Initialize the config first
        self.dbConfig = config.configHandler.DatabaseConfiguration()
        self.version = self.dbConfig.codeVersion
        if print_debug_statements:
            print('Database Config Initialized')
            print('Database Code Version : ' + str(self.version))
            print('Database Config ' + str(self.dbConfig))

        # Initialize the In-Memory Database from a parsed DB
        self.parsedDatabase = dbIo.read_db(self.dbConfig)
        self.inMemoryDatabase = dbIo.generate_object_db_representation(self.dbConfig, self.parsedDatabase)

        print('--- Database Project V:' + str(self.version) + ' ready ---')
        # Read user commands until exit
        self.inputInterpreter = control.userInputInterpreter.CommandInterpreter(self.inMemoryDatabase, self.dbConfig)
        self.inputInterpreter.init_input_reader()

        # TERMINATE PROGRAM
        # On exit, commit changes and close
        print('Committing database to disk')
        dbIo.write_db(self.dbConfig, self.inMemoryDatabase, print_debug_statements)
        # Update the config changes
        print('Committing config changes to disk')
        self.dbConfig.persist_config()
        print('--- Database Project V:' + str(self.version) + ' terminated ---')
