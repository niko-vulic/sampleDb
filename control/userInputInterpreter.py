EXIT = 'exit'
FIND = 'find'

class CommandInterpreter:
    def __init__(self, print_debug_statements=False):
        self.input = ''
        self.print_debug_statements = False

    def parseInput(self, inputString):
