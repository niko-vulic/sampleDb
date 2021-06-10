import config.configHandler
import config.dbConstants

def findItem(itemName, database):
    for item in database:
        if item.name == itemName:
            return item
    return None

class DbCommands:
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
                    return "Price of  "+ str(quantity) + " " + name + " is: $" + str \
                        (quantity * int(item[self.ProjectConfig.priceColumnIndex]))
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
            newItem = [1 ,2 ,3]
            newItem[self.ProjectConfig.nameColumnIndex] = name
            newItem[self.ProjectConfig.priceColumnIndex] = price
            newItem[self.ProjectConfig.typeColumnIndex] = type
            self.database.append(newItem)
            return "Item: " + str(newItem) + " added to database!"