import sys

from .item import Item
class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item 
    
    def remove(self, item):
        print(self.inventory)
        if item in self.inventory:
            self.inventory.remove(item)
            return item 
        else:
            return False
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == Item(category=category).category]