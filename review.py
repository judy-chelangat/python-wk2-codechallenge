from customer import Customer
from restuarant import Restuarant
#    Review __init__()`
 # - Reviews should be initialized with a customer, restaurant, and a rating (a number)
#-  `Review rating()`
 # - returns the rating for a restaurant.
#-  `Review all()`
 # - returns all of the reviews


 #- `Review customer()`
 # - returns the customer object for that review
  #- Once a review is created, should not be able to change the customer
  # `Review restaurant()`
 # - returns the restaurant object for that given review
 # - Once a review is created, should not be able to change the restaurant
class Review(Customer,Restuarant):
    all_reviews=[] #variable to hold all the reviews
    def __init__(self,first_name,restuarant_name,rating):
        self.rating = rating
        self.first_name=first_name
        self.restuarant_name=restuarant_name
        super().__init__(first_name,restuarant_name) #using super to initialize the name from the parent class
        self.all_reviews.append(self)

    def review_rating(self):
        return self.rating
    
    def review_customer(self):
        return self.first_name
    
    def review_restuarant(self):
        return self.restuarant_name
    
    @classmethod
    def review_all(cls):
        return cls.all_reviews
   
   

customer1 = Customer("Judy", "sigilai")
restuarant1=Restuarant("Frangos")

review1=Review(customer1,restuarant1,6) #instance creation
print(review1.review_rating()) #printing the rating

print(Review.review_all())

print(review1.review_customer().full_name())  # retrieving details from the customer class
print(review1.review_restuarant().name()) 