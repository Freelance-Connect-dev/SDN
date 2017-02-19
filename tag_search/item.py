class item:

"""
Author: Scott Franz

Class to store and handle item information. Associated with tags.
"""

    def __init__(self, id):
        """
        Params:
        id 'ID of this item.'
        """
        self.id = id
        
    def __str__(self):
        return str(self.id)