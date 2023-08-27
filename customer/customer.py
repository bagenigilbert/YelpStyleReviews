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
    
    # method to retrieve the full name of the customer
    def get_full_name(self):
        return f"{self.given_name} {self.family_name}"
    
    # method to add a review for a restaurant with  a rating
    def add_review(self,restaurant,rating):
        review = review(self,restaurant,rating)  # Create a new Review instance
        self.reviews.append(review)  # Add the review to the list of reviews for this customer
        restaurant.add_review(review)  # Call the add_review method of the Restaurant class

    
