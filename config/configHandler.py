import configparser
import sys
import os
import logging

import config.dbConstants as dbConst


class DatabaseConfiguration:
    def __init__(self):
        # Read the ini file from local dir
        db_config = configparser.ConfigParser()
        #with open(dbConst.CONFIG_FILE, 'r') as config_file:
        #with open('config/config.ini', 'r') as config_file:
        db_config.read('config/config.ini')

        # Define log levels
        self.logLevel = {}
        self.logLevel[dbConst.DB_IO] = db_config[dbConst.SECT_LOG][dbConst.DB_IO]
        self.logLevel[dbConst.DB_COMMANDS] = db_config[dbConst.SECT_LOG][dbConst.DB_COMMANDS]
        self.logLevel[dbConst.CONF_HANDLER] = db_config[dbConst.SECT_LOG][dbConst.CONF_HANDLER]

        # Set the logger - have to import logger settings first
        logging.basicConfig(stream=sys.stdout, level=self.logLevel[dbConst.CONF_HANDLER])
        logger = logging.getLogger(dbConst.CONF_HANDLER)

        # Set version
        self.codeVersion = db_config['DEFAULT']['codeVersion']

        # Set class-local params
        self.delimiter = db_config['DEFAULT']['delimiter']
        self.format = db_config['DEFAULT']['format']
        self.filename = db_config['DEFAULT']['filename']
        self.columns = self.format.split(self.delimiter)

        self.nameColumnIndex = self.get_column(dbConst.NAME)
        self.priceColumnIndex = self.get_column(dbConst.PRICE)
        self.typeColumnIndex = self.get_column(dbConst.TYPE)

        # Debug statements
        logger.debug('DEBUG - Initializing ConfigHandler')
        logger.debug('DEBUG - DB delimiter:' + db_config.get('DEFAULT', 'delimiter'))
        logger.debug('DEBUG - DB format:' + db_config.get('DEFAULT', 'format'))
        logger.debug('DEBUG - DB filename:' + db_config.get('DEFAULT', 'filename'))
        logger.debug('DEBUG - Config sections:' + str(db_config.sections()))

    def __repr__(self):
        return 'Log levels: ' + str(self.logLevel)

    def update_log_level(self, logger_name, new_log_level):
        # Set the logger - have to import logger settings first
        logging.basicConfig(stream=sys.stdout, level=self.logLevel[dbConst.CONF_HANDLER])
        logger = logging.getLogger(dbConst.CONF_HANDLER)

        update_result = ''

        # Only update if valid logger level:
        if new_log_level in dbConst.VALID_LOG_LEVELS:
            # Only update if valid logger:
            if logger_name in self.logLevel:
                logger.debug('Found ' + logger_name + ' in ' + str(self.logLevel))
                # Read the ini file from local dir and update it
                db_config = configparser.ConfigParser()
                #with open('config/config.ini', 'r') as config_file:
                db_config.read(dbConst.CONFIG_FILE)
                db_config[dbConst.SECT_LOG][logger_name] = new_log_level
                logger.debug('Read in config as: ' + str(db_config))
                logger.debug('Config sections:' + str(db_config.sections()))

                with open(dbConst.CONFIG_FILE, 'w') as config_file_updater:
                    db_config.write(config_file_updater)

                # Also update the in-memory log level
                self.logLevel[logger_name] = new_log_level
                update_result = 'Logger: ' + logger_name + ' updated to log level: ' + new_log_level
            else:
                # invalid logger name
                update_result = 'Invalid logger name, unable to update'
        else:
            # invalid log level
            update_result = "Invalid log level. Must be one of: " + str(dbConst.VALID_LOG_LEVELS)

        return update_result

    # Get column by index, for parsing the DB format from config.ini file
    def get_column(self, name):
        try:
            column_index = self.columns.index(name)
            return column_index
        except ValueError:
            return -1
