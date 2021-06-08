import configparser
import sys
import os

class ProjectConfig:
    def __init__(self, printDebugStatements = False):
        # Read the ini file from local dir
        config = configparser.ConfigParser()
        config.read('config.ini')

        # Set class-local params
        self.delimiter = config['DEFAULT']['delimiter']
        self.format = config['DEFAULT']['format']
        self.filename = config['DEFAULT']['filename']
        self.columns = self.format.split(self.delimiter)

        self.nameColumnIndex = self.getColumn('name')
        self.priceColumnIndex = self.getColumn('price')
        self.typeColumnIndex = self.getColumn('type')

        # Debug statements
        if printDebugStatements:
            print('DEBUG - Initializing')
            print('DEBUG - DB delimiter:' + config.get('DEFAULT', 'delimiter'))
            print('DEBUG - DB format:' + config.get('DEFAULT', 'format'))
            print('DEBUG - DB filename:' + config.get('DEFAULT', 'filename'))

    # Get column by index
    def getColumn(self, name):
        try:
            column_index = self.columns.index(name)
            return column_index
        except:
            return -1

    # Update with a new delimiter
    def setDelimiter(self, newDelimiter):
        if len(newDelimiter) == 1:
            self.delimiter = newDelimiter
        else:
            print("Delimiter must be 1 char")

    # Parse the DB details from txt file
    def parseDb(self, printDebugStatements = False):
        parsedDb = []

        if printDebugStatements:
            print('Parsing the DB')
            print(self.columns)

        # Read each line in the file and split the data into columns
        dbFile = open(self.filename, 'r')
        for line in dbFile:
            formattedLine = line.strip().split(self.delimiter)
            parsedDb.append(formattedLine)

            if printDebugStatements:
                print(formattedLine)
        dbFile.close()

        if printDebugStatements:
            print(parsedDb)
        return parsedDb

    # Write the current DB contents out back to the file
    def updateDb(self, database, printDebugStatements = False):
        dbFile = open(self.filename, 'w')
        lines = []
        for item in database:
            lines.append(str(item[0]) + self.delimiter + str(item[1]) + self.delimiter + str(item[2]))

        # Write out to file
        dbFile.write('\n'.join(lines))
        dbFile.close()






if __name__ == '__main__':
    print('Setup.py main function. For debug purposes, set arg[1] to True')
    # Setup the debug statements value to be passed to sub-functions
    debug = False
    if len(sys.argv) > 1:
        debug = sys.argv[1] == 'True'

    x = ProjectConfig(debug)
    x.parseDb(debug)
