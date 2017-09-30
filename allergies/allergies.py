class Allergies(object):
    allergies = ["eggs", "peanuts", "shellfish", "strawberries", "tomatoes", "chocolate", "pollen", "cats"]

    def __init__(self, number):
        self.rank = number % 256

    def is_allergic_to(self, string):
        return (self.rank & pow(2, self.allergies.index(string))) != 0

    @property
    def lst(self):
        return [ x for x in self.allergies if self.is_allergic_to(x)]
