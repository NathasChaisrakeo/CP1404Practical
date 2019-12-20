class ProgrammingLanguage:

    def __init__(self, name, typing, reflection, year):
        """Constriuctor that takes in parameters and create object"""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determines if a language is dynamically or statically typed"""
        if self.typing == "Dynamic":
            return True

    def __str__(self):
        """Return the details of the object in string format"""
        return "{}, {} Typing, Reflection= {}, First appeared in {}".format(
            self.name, self.typing, self.reflection, self.year)

