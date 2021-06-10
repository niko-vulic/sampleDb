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