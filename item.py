class Item():
#Item constructor method
    def __init__(self, name):
        self._name = name
        self._description =  None

    #Getter for the item name
    @property
    def name(self):
        """
        This property gets an item name
        """
        return self._name

    #Setter for the item name
    @name.setter
    def name(self, item_name):
        """
        This property sets an item name
        """
        self._name = item_name

    #Getter for the item description
    @property
    def description(self):
        """
        This property gets an item description
        """
        return self._description

    #Setter for the item description
    @description.setter
    def description(self, item_description):
        """
        This property sets an item description
        """
        self._description = item_description

    #Getter for item details
    def item_details(self):
        """
        This method prints an item description
        """
        print('___________________________')
        print('Item found!')
        print(self._description + " [take]")