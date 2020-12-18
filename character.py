#Superclass
class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        """
        This method prints a character description. For an enemy "talk" and "fight" are options. For a friend "talk" is the only option.
        """
        print( self.name + " is here!" )
        if self.name != 'Susan':
            print( self.description + " [talk] [fight]")
        else:
            print( self.description + " [talk]")

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        """
        This method is used to set what a character will say when talked to
        """
        self.conversation = conversation

    # Character conversation
    def talk(self):
        """
        This method is used to set a character conversation
        """
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation + " [ok]")
        else:
            print(self.name + " doesn't want to talk to you")

#Subclass
#The name of this new class is Enemy.
#Putting Character inside the brackets tells Python that
#the Enemy class will inherit all of the methods from Character.
class Enemy(Character):
    """
    This is a subclass of the superclass Character to create enemies
    """
    #Class variable
    number_of_enemies = 0
    """
    This is a class variable used to count how many enemies has been created
    """
    def __init__(self, char_name, char_description):
        #To make an Enemy, first make a Character object and then I will customise it.
        #When the __init__() function is created in a subclass,
        #the subclass will no longer inherit the superclass’s __init__() function.
        #Calling the previously built methods with super()
        #saves you from needing to rewrite those methods in your subclass.
        super().__init__(char_name, char_description)
        #Customized methods
        self.weakness = None
        Enemy.number_of_enemies = Enemy.number_of_enemies + 1

    # Set the character weakness
    def set_weakness(self, weakness):
        """
        This method is used to set an enemy character weakness
        """
        self.weakness = weakness

    def fight(self):
        """
        This method is used to get an input of the user about the combat item to use against an enemy character.
        It returns a combat item
        """
        print('What are you going to use to fight?')
        combat_item = input("> ")
        return combat_item

    def check_result(self, combat_item):
        """
        This method is used to check the fight results.
        It returns True when the combat item == enemy weakness
        It returns False when the combat item != enemy weakness
        """
        if combat_item == self.weakness:
            print()
            print("You fend " + self.name + " off with the " + combat_item)
            return True
        else:
            print()
            print(self.name + " crushes you, puny adventurer")
            return False

class Friend(Character):
    """
    This is a subclass of the superclass Character to create friends
    """
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.gift = None

    def set_gift(self, gift):
        """
        This is a method to set a gift to a friend character
        """
        self.gift = gift

    def get_gift(self):
        """
        This is a method to get a gift from a friend character
        """
        return self.gift