import configparser
import sys
import os
import logging

import config.dbConstants


class DatabaseConfiguration:
    def __init__(self, print_debug_statements=False):
        # Read the ini file from local dir
        db_config = configparser.ConfigParser()
        db_config.read('config/config.ini')

        # Define log levels
        self.logLevel = {}
        self.logLevel[config.dbConstants.DB_IO] = db_config[config.dbConstants.SECT_LOG][config.dbConstants.DB_IO]
        self.logLevel[config.dbConstants.DB_COMMANDS] = db_config[config.dbConstants.SECT_LOG][config.dbConstants.DB_COMMANDS]
        self.logLevel[config.dbConstants.CONF_HANDLER] = db_config[config.dbConstants.SECT_LOG][config.dbConstants.CONF_HANDLER]

        # Set the logger - have to import logger settings first
        logging.basicConfig(stream=sys.stdout, level=self.logLevel[config.dbConstants.CONF_HANDLER])
        logger = logging.getLogger(config.dbConstants.CONF_HANDLER)

        # Set version
        self.codeVersion = db_config['DEFAULT']['codeVersion']

        # Set class-local params
        self.delimiter = db_config['DEFAULT']['delimiter']
        self.format = db_config['DEFAULT']['format']
        self.filename = db_config['DEFAULT']['filename']
        self.columns = self.format.split(self.delimiter)

        self.nameColumnIndex = self.get_column(config.dbConstants.NAME)
        self.priceColumnIndex = self.get_column(config.dbConstants.PRICE)
        self.typeColumnIndex = self.get_column(config.dbConstants.TYPE)

        # Debug statements
        if print_debug_statements:
            logger.debug('DEBUG - Initializing ConfigHandler')
            logger.debug('DEBUG - DB delimiter:' + db_config.get('DEFAULT', 'delimiter'))
            logger.debug('DEBUG - DB format:' + db_config.get('DEFAULT', 'format'))
            logger.debug('DEBUG - DB filename:' + db_config.get('DEFAULT', 'filename'))

    def __repr__(self):
        return 'Log levels: ' + str(self.logLevel)

    # Get column by index, for parsing the DB format from config.ini file
    def get_column(self, name):
        try:
            column_index = self.columns.index(name)
            return column_index
        except ValueError:
            return -1
