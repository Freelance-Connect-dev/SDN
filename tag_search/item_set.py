from tag import tag
from item import item

class item_set():
    """
    Author: Scott Franz
    
    Purpose: Assistant data structure for sorting lists of tags.
    """
    
    def __init__(self, item, tag_set=set()):
        self.item = item
        self.tag_set = tag_set
        
    def add_item(self, item):
        tag_set.add(item)
        
    def get_weight(self):
        weight = 0.0
        for tag in self.tag_set:
            weight += tag.weight
        return weight
        
    