class tag():
    """
    Author: Scott Franz
    Base tag class for other tag types in tag_search.
    Params:
    self.id 'String id of tag.'
    self.weight 'Float weight of object.'
    self.link_array 'List of tags or objects this tag is
    associated with.'
    """
    
    def __init__(self, id, weight, link_array):
        self.id = id
        self.weight = weight
        self.link_array = link_array
    
        
    def __str__(self):
        return "tag::tag(" + str(self.id) + "," + str(self.weight) + "," + str(self.link_array) + ")"
        
    def add_link(self, other):
        """Add a reference to another tag or other object.
        Params:
        other 'Other object this tag should link to.'
        """
        
        self.link_array.append(other)
        
    
    