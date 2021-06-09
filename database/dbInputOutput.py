import sys
import os

class DbInputOutput:
    # Parse the DB details from txt file
    def readDb(self, databaseConfig, printDebugStatements=False):
        parsedDb = []

        if printDebugStatements:
            print('Parsing the DB')
            print(databaseConfig.columns)

        # Read each line in the file and split the data into columns
        dbFile = open(databaseConfig.filename, 'r')
        for line in dbFile:
            formattedLine = line.strip().split(databaseConfig.delimiter)
            parsedDb.append(formattedLine)

            if printDebugStatements:
                print(formattedLine)
        dbFile.close()

        if printDebugStatements:
            print(parsedDb)
        return parsedDb

    # Write the current DB contents out back to the file
    def writeDb(self, database, printDebugStatements=False):
        dbFile = open(self.filename, 'w')
        lines = []
        for item in database:
            lines.append(str(item[0]) + self.delimiter + str(item[1]) + self.delimiter + str(item[2]))

        # Write out to file
        dbFile.write('\n'.join(lines))
        dbFile.close()