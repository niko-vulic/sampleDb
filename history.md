1.8
---
- Added a default_db.txt file to prevent database changes getting persisted into GIT and give a starting point if no DB file is found

1.7.2
---
- Simplified config, removed references to format and delimiter being user defined.

1.7.1
---
- Minor bugfix as adding items only accepted integers for price, not floats

1.7
---
- Goal to simplify config, remove user control over delimiter and [name, price, type] columns

1.6.9
---
- Only backup config if items are changed between current config and in-memory
- TODO - make the changes so that codeVersion needs to be kept updated in only 1 place

1.6.8.2
---
- Additional minor changes to loggers to update to new configuration
-- Fixed all loggers on dbInputOutput.py
-- Converted userInputInterpreter to use logging instead of print_debug_statements

1.6.8.1
---
- Bug fixes to setting logLevel. logging.basicConfig() is only invoked once with log.setLevel used properly

1.6.8
---
- Changed configHandler to persist changes upon exit only rather than upon every log level change.
- Added a config/backup/ directory to create backups of every config change
- Moved configHandler.logger to the 'self' level - unsure if this is a good design pattern so far

1.6.7
---
- Added a defaultConfig.ini file which will be used to form config.ini so changes to config.ini don't get saved to git
- Implemented .gitignore for the first time

1.6.5
---
- Added ability to update logger levels from default values
- Added writing config file changes back out to disc
-- Bug, cannot open config file with: with open(dbConst.CONFIG_FILE, 'r') as config_file:

1.6.3
---
- Started logging implementation of configHandler

1.6.1
---
- Redo of dbInputOutput.read_db to use logging framework instead of print_debug_statements

1.6
---
- Redo of logging and debug statements to make use of Python logger framework.

1.5.5
---
- Added write_db function to persist session changes to disk.

1.5.4
---
- Added DELETE functionality. Command interpreter complete. Next task: write DB per config, add additional commands for CONFIG + LOGGING setup
- Refactor dbCommands.py to satisfy PEP8 styling

1.5.3
---
- Added LIST command functionality to verify database contents to be able to proceed on ADD functionality.
- Fully implemented ADD and UPDATE functionality to UI and DB operations

1.5.2
---
- Improved upon ADD functionality to parse user input with exception handling and search for an existing item. Next step: fully implement to ADD or UPDATE the inputted item

1.5
---
- Created a [databaseItem] class to better represent the object, rather than parsing over a list and column indices. This makes it easier to iterate over the database rather than having to pass the databaseConfiguration object into each method and calculate column indices. 

1.4.2
---
- Added constants to class configHandler for column names to be re-used in userInputInterpreter


1.4.1
---
- Continue to build command interpreter. Move functionality from dbInterface to userInputInterpreter sub-class

1.4
---
- Begin to create a command interpreter which can call dbCommands.py to execute certain commands on the IMDB (in-memory database)

1.3
---
- Got packages somewhat working. Still don't fully understand them
- Resolved an issue by making dbInputOutput.py a static function rather than in the DbInputOutput class

1.2.1
---
-DbInputOutput added functions for:
- ReadDb() - reading in database
- WriteDb() - writing to file

1.2
---
-Separated DB functions into their own subclasses
- InputOutput class for reading writing
- Commands class for modifying the DB

1.1
---
- Separated config handling into its own class

1.0
---
- Initial import