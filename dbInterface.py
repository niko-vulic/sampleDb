from config import configHandler

class DbInterface:
    def __init__(self, printDebugStatements = False):
        self.ConfigHandler = configHandler.ConfigHandler("True")