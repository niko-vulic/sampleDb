import configparser
import sys
import os

COLUMN_NAME = 'name'
COLUMN_PRICE = 'price'
COLUMN_TYPE = 'type'


class DatabaseConfiguration:
    def __init__(self, printDebugStatements=False):
        # Read the ini file from local dir
        config = configparser.ConfigParser()
        config.read('config/config.ini')

        # Set version
        self.codeVersion = config['DEFAULT']['codeVersion']

        # Set class-local params
        self.delimiter = config['DEFAULT']['delimiter']
        self.format = config['DEFAULT']['format']
        self.filename = config['DEFAULT']['filename']
        self.columns = self.format.split(self.delimiter)

        self.nameColumnIndex = self.get_column(COLUMN_NAME)
        self.priceColumnIndex = self.get_column(COLUMN_PRICE)
        self.typeColumnIndex = self.get_column(COLUMN_TYPE)

        # Debug statements
        if printDebugStatements:
            print('DEBUG - Initializing ConfigHandler')
            print('DEBUG - DB delimiter:' + config.get('DEFAULT', 'delimiter'))
            print('DEBUG - DB format:' + config.get('DEFAULT', 'format'))
            print('DEBUG - DB filename:' + config.get('DEFAULT', 'filename'))

    # Get column by index, for parsing the DB format from config.ini file
    def get_column(self, name):
        try:
            column_index = self.columns.index(name)
            return column_index
        except:
            return -1


if __name__ == '__main__':
    print('configHandler.py main function. For debug purposes, set arg[1] to True')
    # Setup the debug statements value to be passed to sub-functions
    debug = False
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'True'

    x = ConfigHandler(debug)
