from customer import Customer
from restuarant import Restuarant
#    Review __init__()`
 # - Reviews should be initialized with a customer, restaurant, and a rating (a number)
#-  `Review rating()`
 # - returns the rating for a restaurant.
#-  `Review all()`
 # - returns all of the reviews
class Review(Customer,Restuarant):
    all_reviews=[] #variable to hold all the reviews
    def __init__(self,rating,first_name,last_name):
        self.rating = rating
        super().__init__(first_name,last_name)
    def review_rating(self):
        return self.rating
    
    @classmethod
    def review_all(cls):
        return cls.all_reviews

