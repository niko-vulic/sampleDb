import setup

class DbQuery:
    def __init__(self, printDebugStatements = False):
        self.ProjectConfig = setup.ProjectConfig()
        self.database = self.ProjectConfig.parseDb()




        if self.ProjectConfig.nameColumnIndex < 0 or self.ProjectConfig.priceColumnIndex < 0:
            raise Exception("Database configured incorrectly. No name or price column found!")

        # Optional debugging
        if printDebugStatements:
            print('Database initialized: ' + str(self.database))
            print('Database columns: ' + str(self.ProjectConfig.columns))
            print('Price Column index:' + str(self.ProjectConfig.priceColumnIndex))
            print('Name Column index:' + str(self.ProjectConfig.nameColumnIndex))
            print('Type Column index:' + str(self.ProjectConfig.typeColumnIndex))

    def exit(self):
        print("Committing database!")
        self.ProjectConfig.updateDb(self.database)
        print("Database committed, exiting now!")


    ###########################
    ## Database functions below
    ###########################

    def getPriceOfItem(self, name, quantity = 1):
        """Returns the item's price multiplied by the optional quantity"""
        for item in self.database:
            if item[self.ProjectConfig.nameColumnIndex] == name:
                if quantity == 1:
                    return "Price of " + name + " is: $" + str(item[self.ProjectConfig.priceColumnIndex])
                else:
                    return "Price of "+ str(quantity) + " " + name + " is: $" + str(quantity * int(item[self.ProjectConfig.priceColumnIndex]))
        return "Item: " + name + " not found!"

    def addItemToDatabase(self, name, price, type = 'uncategorized'):
        """Add the item to the database with the specified price and type"""
        itemFound = False
        for item in self.database:
            # Try to find the item first, if it already exists
            if item[self.ProjectConfig.nameColumnIndex] == name:
                itemFound = True
                item[self.ProjectConfig.priceColumnIndex] = price
                item[self.ProjectConfig.typeColumnIndex] = type
                return "Item: " + name + " updated!"

        if not itemFound:
            newItem = [1,2,3]
            newItem[self.ProjectConfig.nameColumnIndex] = name
            newItem[self.ProjectConfig.priceColumnIndex] = price
            newItem[self.ProjectConfig.typeColumnIndex] = type
            self.database.append(newItem)
            return "Item: " + str(newItem) + " added to database!"


if __name__ == '__main__':
    queryClass = DbQuery(True)
