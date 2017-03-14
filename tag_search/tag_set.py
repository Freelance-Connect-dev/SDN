"""
Author: Scott Franz

Tag list to store a list of tags drawn from data base.
"""

from tag import tag
from item import item

class tag_set():

    """
    List to store tags in.
    This class is also supposed to handle database query and saves.
    """
    
    def __init__(self):
        self.tdict = {}
        
    def add(self, tag):
        """
        Method to add a tag_pair to this tag_list and handle all
        database query and save requests to assure that
        the script and the database contain the same tags.
        """
        self.tdict[tag.id] = tag
        
    def load_from_csv(self, file_name):
        """
        Method to load test file from csv.
        """
        with open(file_name, "r") as ifile:
            for line in ifile:
                lparts = line.rstrip().split(",")
                # print(lparts)
                tag_id = lparts[0]
                # print(tag_id)
                tag_weight = lparts[1]
                # print(tag_weight)
                atag = tag(tag_id, tag_weight)
                for i in range(2, len(lparts)):
                    # print(lparts[i])
                    atag.add_item(item(lparts[i]))
                    
                self.add(atag)
                
if __name__ == '__main__':
    ts = tag_set()
    ts.load_from_csv("./tests/tags1.csv")
                