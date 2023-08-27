#define the customer  class
class Customer:
#Initialize a customer object with given_name and family_name
    def __init__(self, given_name, family_name):
        #instances attributes
        self.given_name = given_name
        self.family_name = family_name
        self.reviews = [] # A list to store reviews left by this customer

    # methods to retrieve the given name of the customer
    def  get_given_name(self):
        return self.given_name
    # method to retrieve the family name of the customer
    def get_family_name(self):
        return self.family_name
