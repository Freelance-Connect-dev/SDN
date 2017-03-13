"""
Author: Scott Franz

Tag list to store a list of tags drawn from data base.
"""

from tag import tag
from item import item
from item_list import item_list

class tag_list():

    """
    List to store tags in.
    This class is also supposed to handle database query and saves.
    """
    
    def __init__(self):
        self.tlist = []

    def __init__(self, item_list):
        self.tag_list = []
        self.item_list = item_list
        
    def add(self, tag):
        """
        Method to add a tag_pair to this tag_list and handle all
        database query and save requests to assure that
        the script and the database contain the same tags.
        """
        self.tlist.append(tag)
        
    def load_from_csv(self, file_name):
        """
        Method to load test file from csv.
        """
        with open(file_name, "r") as ifile:
            for line in ifile:
                lparts = line.rstrip().split(",")
#                print(lparts)
                tag_id = lparts[0]
#                print(tag_id)
                tag_weight = lparts[1]
#                print(tag_weight)
                atag = tag(tag_id, tag_weight)
                for i in range(2, len(lparts)):
#                    print(lparts[i])
                    atag.add_item(item(lparts[i]))
                    
                self.tlist.append(atag)
                
        print(self.tlist)
#                print(tag_weight)S
                tag_links = []
                for i in range(2, len(lparts)):
#                    print(lparts[i])
                    t_item = self.item_list.search_by_id(lparts[i])
                    if(t_item != None):
                        tag_links.append(t_item)
                    
                atag = tag(tag_id, tag_weight, tag_links)
                    
if __name__ == '__main__':
    ilist = item_list()
    ilist
    tl = tag_list()
    tl.load_from_csv("./tests/tags1.csv")
                