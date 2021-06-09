from config import configHandler
from database import dbInputOutput

class DbInterface:
    def __init__(self, printDebugStatements = False):
        self.databaseConfig = configHandler.ConfigHandler(printDebugStatements)
        self.inMemoryDatabase = dbCommands.parseDb(self.databaseConfig, printDebugStatements)

        if printDebugStatements:
            print('Database Config Initialized')
            print('NameColumnIndex:' + str(self.databaseConfig.nameColumnIndex))