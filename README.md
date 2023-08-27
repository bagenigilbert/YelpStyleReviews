# Yelp-Style Reviews System
## Yelp-Style Reviews

#### Author: Gilbert Bageni
#### Contact: gilbertwilber0@gmail.com

## Overview
Welcome to the Yelp-Style Reviews System, a Python-based application that models a simplified version of the Yelp platform for restaurants. This project focuses on creating and managing relationships between Customers, Restaurants, and Reviews, offering a glimpse into the world of object-oriented programming and data associations.

## Features
Customer Management: Create and manage customer profiles, including given names and family names.
Restaurant Information: Define and maintain restaurant details such as names.
Review System: Allow customers to leave reviews for restaurants with ratings.
Data Association: Form relationships between customers, restaurants, and reviews.
Rating Aggregation: Calculate average star ratings for restaurants based on their reviews.
Installation
### Clone the repository to your local machine using:
 git clone https://github.com/yourusername/YelpStyleReviews.git

### Navigate to the project directory:
cd YelpStyleReviews

### Install the required dependencies using Pipenv:
 pipenv run python main.py

### Run the main script:
pipenv run python main.py

## Usage
Create customer and restaurant instances using the provided classes.
Initialize review instances with customers, restaurants, and ratings.
### Use methods to retrieve and manipulate data:
get_full_name(): Get customer's full name.
get_name(): Get restaurant's name.
get_rating(): Get review's rating.
add_review(): Associate a review with a customer and a restaurant.
get_reviews(): Get all reviews for a restaurant.
get_customer(): Get the customer associated with a review.
get_restaurant(): Get the restaurant associated with a review.
average_star_rating(): Calculate the average star rating for a restaurant.
### Example

from customer.customer import Customer
from review.review import Review
from restaurant.restaurant import Restaurant

# Create instances
customer1 = Customer("Gilbert", "Nail")
restaurant1 = Restaurant("Delicious Foods")
review1 = Review(customer1, restaurant1, 4)

# Use methods
print("Customer name:", customer1.get_full_name())
print("Restaurant name:", restaurant1.get_name())
print("Review rating:", review1.get_rating())

# Adding a review
customer1.add_review(restaurant1, 5)
print("Restaurant reviews:", restaurant1.get_reviews())

# Calculating average rating
average_rating = restaurant1.average_star_rating()
print("Average rating:", average_rating)

## Contribution
Contributions are welcome! If you find any issues or want to add enhancements, feel free to fork the repository and create a pull request.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries or suggestions, please contact Gilbert Bageni at gilbertwilber0@gmail.com.


