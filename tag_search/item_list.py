class item_list:

    """
    Author: Scott Franz

    List to contain item references along with handle query and store operations from db.
    """

    def __init__(self):
        self.item_list = []
        
    def add(self, item):
        """
        Add item to this item_list.
        """
        self.item_list.append(item)
        
    def load_from_csv(self, file_name):
        with open(file_name, "r") as file:
            for line in file:
                #FIXME
                lpart = line.rstrip().split(",")
#                print(lpart[0])
                
    def search_by_id(self, id_str):
        for item in self.item_list:
            if item.id == id_str:
                return item
        return None
                
                
if __name__ == '__main__':
    il = item_list()
    il.load_from_csv("./tests/items1.csv")
                