
from tag import tag
from item import item
from tag_list import tag_list
from item_set import item_set

class tag_sort():
    """
    Author: Scott Franz
    Class to handle tag search in python.
    """
        
    def sort(self, t_list):
        S = set()
        for t in t_list.tlist:
            S = S | t.items
            print(S)
#            for item in tag.items:
#                tmp_item = set(item) & S
            
        
       
        
    
        
        
if __name__ == "__main__":
    tl = tag_list()
    tl.load_from_csv("./tests/tags1.csv")
    
    ts = tag_sort()
    ts.sort(tag_list)
