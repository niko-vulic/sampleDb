import sys
import os


class DatabaseItem:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def __repr__(self):
        return 'Item name: ' + self.name + ', price: ' + str(self.price) + ' , type:' + self.type


# Parse the DB details from txt file
def read_db(dbConfig, print_debug_statements=False):
    parsedDb = []

    if print_debug_statements:
        print('Parsing the DB')
        print(dbConfig.columns)

    # Read each line in the file and split the data into columns
    db_file = open(dbConfig.filename, 'r')
    for line in db_file:
        formattedLine = line.strip().split(dbConfig.delimiter)
        parsedDb.append(formattedLine)

        if print_debug_statements:
            print(formattedLine)
    db_file.close()

    if print_debug_statements:
        print(parsedDb)
    return parsedDb


# Create a List[DatabaseItem] representation of the parsed DB
def generate_object_db_representation(dbConfig, parsedDb, print_debug_statements=False):
    database = []
    for item in parsedDb:
        newDbItem = DatabaseItem(item[dbConfig.nameColumnIndex], item[dbConfig.priceColumnIndex], item[dbConfig.typeColumnIndex])
        database.append(newDbItem)

    if print_debug_statements:
        for item in database:
            print('DEBUG - ' + repr(item))
    return database

# Write the current DB contents out back to the file
def write_db(dbConfig, database, print_debug_statements=False):
    db_file = open(dbConfig.filename, 'w')
    lines = []
    for item in database:
        lines.append(str(item.name) + dbConfig.delimiter + str(item.price) + dbConfig.delimiter + str(item.type))

    # Write out to file
    db_file.write('\n'.join(lines))
    db_file.close()
