class RPGInfo():

    rooms = None
    author = "Anonymous"

    def __init__(self, game_title):
        self.title = game_title

    def welcome(self):
        """
        This method prints a welcome message with the title of the game
        """
        print("WELCOME TO " + self.title)

    @staticmethod
    def info():
        """
        This static method prints information about game creation
        """
        print("Made using the OOP RPG Creator (c) me")

    @classmethod
    def game_goal(cls):
        """
        This class method prints information about the game goal using the class variable rooms
        """
        print()
        print('You will need to explore the ' + cls.rooms + ' rooms in the castle to fight Dorian who hates the light, fight Dave who hates the cheese and release their prisioner Susan. A gift is waiting for you!')
        print('Good luck!')

    @staticmethod
    def game_over():
        """
        This static method prints game over information
        """
        print ("Susan is dead")
        print("GAME OVER")

    @classmethod
    def credits(cls):
        """
        This class method prints credits information using the class varibale author
        """
        print()
        print("Thank you for playing")
        print("Created by " + cls.author)