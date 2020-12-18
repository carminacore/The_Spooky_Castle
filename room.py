class Room():

#Class variable
    number_of_rooms = 0

#Constructor method for a class
#By using self, a method can invoke the object
#and access the attributes and methods of that object
    def __init__(self, room_name):
        self.name = room_name
        self._description = None
        self.linked_rooms = {}
        self.character = None
        self.item = None
        Room.number_of_rooms = Room.number_of_rooms + 1

#Description methods

    #Getter for description
    @property
    def description(self):
        """
        This method is used to get a room description
        """
        return self._description

    #Setter for description
    @description.setter
    def description(self, room_description):
        """
        This method is used to set a room description
        """
        self._description = room_description

#Name methods
    #Setter for name
    def set_name(self, room_name):
        """
        This method is to set a room name
        """
        self.name = room_name

    #Getter for name
    def get_name(self):
        """
        This method is to get a room name
        """
        return self.name

#Character methods
    def set_character(self, new_character):
        """
        This method is to set a character in a room
        """
        self.character = new_character

    def get_character(self):
        """
        This method is to get a character from a room
        """
        return self.character

    def describe(self):
        """
        This method prints a character description
        """
        print(self.description)

#Item methods
    def set_item(self, new_item):
        """
        This method is to set an item in a room
        """
        self.item = new_item

    def get_item(self):
        """
        This method is to get an item from a room
        """
        return self.item

    def item_details(self):
        """
        This method prints an item description
        """
        print(self._description)

#Linked rooms methods
    def link_room(self, room_to_link, direction):
        """
        This method is to link a room with an available direction
        """
        self.linked_rooms[direction] = room_to_link

#Details method
    def get_details(self):
        """
        This method prints the room description and the linked rooms
        """
        print('___________________________')
        print(self.name)
        print(self.description)
        for direction in self.linked_rooms:
            #You need to invoke the getter get_name() from the method self.linked_rooms[direction]
            print("The " + self.linked_rooms[direction].get_name() + " is " + "[" + direction + "]")

#Move method
    def move(self, direction):
        """
        This method allows moving to other room
        """
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self