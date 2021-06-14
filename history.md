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