class Chat:
    """
    A class representing a cat that can meow and perform other actions.
    """
    def __init__(self, name):
        self.name = name

    def meow(self):
        return f"{self.name} says Meow!"

