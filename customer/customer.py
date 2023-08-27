#define the customer  class
class Customer:
#Initialize a customer object with given_name and family_name
    def __init__(self, given_name, family_name):
        #instances attributes
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = []