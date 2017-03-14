
from tag import tag
from item import item
from tag_set import tag_set
from collections import OrderedDict

class tag_search():
    """
    Author: Scott Franz
    Class to handle tag search in python.
    """
        
    def sort(self, t_set):
        S = {}
        for k, v in t_set.tdict.iteritems():
            for itm in v.items:
                if itm.id not in S:
                    S[itm.id] = v.weight
                else:
                    S[itm.id] += v.weight
       
        S = OrderedDict(sorted(S.items(), key=lambda x: x[1]))
        print(S)
                    
                
                


if __name__ == "__main__":
    tl = tag_set()
    tl.load_from_csv("./tests/tags1.csv")
    
    ts = tag_search()
    ts.sort(tl)
