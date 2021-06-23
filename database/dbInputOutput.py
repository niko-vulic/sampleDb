import sys
import os
import logging
import config.dbConstants as dbConst


class DatabaseItem:
    def __init__(self, name, price, type):
        self.name = name
        self.price = price
        self.type = type

    def __repr__(self):
        return 'Item name: ' + self.name + ', price: ' + str(self.price) + ' , type:' + self.type


# Parse the DB details from txt file
def read_db(dbConfig):
    logger = logging.getLogger(dbConst.DB_IO)
    logger.setLevel(dbConfig.logLevel[dbConst.DB_IO])
    parsed_db = []

    logger.info('Parsing the database from disk...')
    logger.debug('DB columns: ' + str(dbConfig.columns))

    # Read each line in the file and split the data into columns
    db_file = open(dbConfig.filename, 'r')
    for line in db_file:
        formatted_line = line.strip().split(dbConfig.delimiter)
        parsed_db.append(formatted_line)
        logger.debug('Reading DB - next line:' + str(formatted_line))

    db_file.close()

    logger.debug('Parsed DB:' + str(parsed_db))
    return parsed_db


# Create a List[DatabaseItem] representation of the parsed DB
def generate_object_db_representation(dbConfig, parsed_db):
    logger = logging.getLogger(dbConst.DB_IO)
    logger.setLevel(dbConfig.logLevel[dbConst.DB_IO])

    database = []
    for item in parsed_db:
        new_db_item = DatabaseItem(item[dbConfig.nameColumnIndex], item[dbConfig.priceColumnIndex], item[dbConfig.typeColumnIndex])
        database.append(new_db_item)

    logger.debug('Database formatted as DatabaseItem classes:')
    for item in database:
        logger.debug(repr(item))
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
