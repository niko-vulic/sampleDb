import configparser
import sys
import os
from os import path
import shutil
import logging

from time import time
from datetime import datetime

import config.dbConstants as dbConst


class DatabaseConfiguration:
    def __init__(self):
        db_config = configparser.ConfigParser()
        logging.basicConfig(stream=sys.stdout)

        # Attempt to read the config.ini file from local dir
        if path.exists(dbConst.CONFIG_FILE):
            print('ConfigHandler - reading from config.ini file')
            db_config.read(dbConst.CONFIG_FILE)
        # 1.6.7 - if default config file does not exist, read default_config.ini file instead
        else:
            print('ConfigHandler - Config.ini not found, generating for the first time')
            db_config.read(dbConst.DEFAULT_CONFIG_FILE)
            with open(dbConst.CONFIG_FILE, 'w') as config_file_updater:
                db_config.write(config_file_updater)

        # Define log levels
        self.logLevel = {}
        self.logLevel[dbConst.DB_IO] = db_config[dbConst.SECT_LOG][dbConst.DB_IO]
        self.logLevel[dbConst.DB_COMMANDS] = db_config[dbConst.SECT_LOG][dbConst.DB_COMMANDS]
        self.logLevel[dbConst.CONF_HANDLER] = db_config[dbConst.SECT_LOG][dbConst.CONF_HANDLER]
        self.logLevel[dbConst.USER_COMMANDS] = db_config[dbConst.SECT_LOG][dbConst.USER_COMMANDS]

        # Set the logger - have to import logger settings first
        self.logger = logging.getLogger(dbConst.CONF_HANDLER)
        self.logger.setLevel(self.logLevel[dbConst.CONF_HANDLER])

        # Set version
        self.codeVersion = db_config['DEFAULT']['codeVersion']

        # Set class-local params
        self.delimiter = db_config['DEFAULT']['delimiter']
        self.format = db_config['DEFAULT']['format']
        self.filename = db_config['DEFAULT']['filename']

        # 1.7 - Format will be statically defined. Format = name,price,type
        self.nameColumnIndex = dbConst.NAME_VALUE
        self.priceColumnIndex = dbConst.PRICE_VALUE
        self.typeColumnIndex = dbConst.TYPE_VALUE

        # Debug statements
        self.logger.info('Initializing ConfigHandler')
        self.logger.debug('DEBUG - DB delimiter:' + db_config.get('DEFAULT', 'delimiter'))
        self.logger.debug('DEBUG - DB format:' + db_config.get('DEFAULT', 'format'))
        self.logger.debug('DEBUG - DB filename:' + db_config.get('DEFAULT', 'filename'))
        self.logger.debug('DEBUG - Config sections:' + str(db_config.sections()))

    def __repr__(self):
        return 'Log levels: ' + str(self.logLevel)

    # Note: we do not compare the logger itself as this is set once upon class creation
    # By comparing code versions, going forward we only need to keep defaultConfig.ini updated
    def __eq__(self, other):
        return isinstance(other, self.__class__) and \
            self.logLevel == other.logLevel and self.codeVersion == other.codeVersion and \
            self.delimiter == other.delimiter and self.format == other.format and self.filename == other.filename

    def update_log_level(self, logger_name, new_log_level):
        update_result = ''

        # Only update if valid logger level:
        if new_log_level in dbConst.VALID_LOG_LEVELS:
            # Only update if valid logger:
            if logger_name in self.logLevel:
                self.logger.debug('Found ' + logger_name + ' in ' + str(self.logLevel))
                # Update the in-memory log level
                self.logLevel[logger_name] = new_log_level
                update_result = 'Logger: ' + logger_name + ' updated to log level: ' + new_log_level
            else:
                # invalid logger name
                update_result = 'Invalid logger name, unable to update'
        else:
            # invalid log level
            update_result = "Invalid log level. Must be one of: " + str(dbConst.VALID_LOG_LEVELS)

        return update_result

    # Persist the config changes, to be called upon exit
    def persist_config(self):
        if self.is_config_backup_required():
            # Backup the existing conf file first into the backup dir
            backup_file_name = 'config-' + str(datetime.fromtimestamp(time()).strftime("%Y%m%d-%H%M%S")) + '.ini.'
            shutil.copy(dbConst.CONFIG_FILE, 'config/backup/' + backup_file_name)
            
            self.logger.debug('Backup filename:' + backup_file_name)
            self.logger.warning('Existing config file backed up due to changes')

            # Create a configParser from the existing config.ini to use as a base to update
            temp_config_parser = configparser.ConfigParser()
            temp_config_parser.read(dbConst.CONFIG_FILE)
            # Update the config with the in-memory logger levels:
            for logger_name in self.logLevel:
                self.logger.debug('Logger ' + logger_name + ' . Old:' + str(temp_config_parser[dbConst.SECT_LOG][logger_name]) + ', new:' + str(self.logLevel[logger_name]))
                temp_config_parser[dbConst.SECT_LOG][logger_name] = self.logLevel[logger_name]

            # Write the updated temp_config_parser back to disk
            with open(dbConst.CONFIG_FILE, 'w') as config_file_writer:
                temp_config_parser.write(config_file_writer)
        else:
            self.logger.info('Config not updated on disk, no changes made!')

    def is_config_backup_required(self):
        # Create a temporary config to compare against the in-memory version
        # Note we only compare logger level changes.
        temp_db_config = DatabaseConfiguration()
        
        # If both configs are the same, no update is required
        if self.__eq__(temp_db_config):
            self.logger.debug('Config object is same as disk version')
            return False

        self.logger.debug('Config object is different from disk version')
        return True
