def find_item(item_name, database):
    """Returns an item from the DB if it exists, else None"""
    for item in database:
        if item.name == item_name:
            return item
    return None


def add_item(item, database):
    """Appends an item to the end of the database"""
    database.append(item)


def update_item(new_item, database):
    """Updates an item to the end of the database"""
    for item in database:
        if item.name == new_item.name:
            item.price = new_item.price
            item.type = new_item.type


def delete_item(item_to_delete_name, database):
    """Attempt to delete an item. Return true if successful"""
    for item in database:
        if item.name == item_to_delete_name:
            database.remove(item)
            return True
    return False
