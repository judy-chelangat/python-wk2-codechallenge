# Restaurant __init__()`
# - Restaurants should be initialized with a name, as a string
#- `Restaurant name()`
# - returns the restaurant's name
#- should not be able to change after the restaurant is created

#`  Restaurant reviews()`
 # -returns a list of all reviews for that restaurant
#- `Restaurant customers()`
 # -Returns a **unique** list of all customers who have reviewed a particular restaurant.


class Restuarant():
    def __init__(self,restuarant_name): #initialized the restuarant with a name
        self.restuarant_name=restuarant_name
        self.reviews=[] #stores the reviews associated with the restuarant 

    def name(self):
        return self.restuarant_name
    
    def reviews(self): #returns a list of all the reviews 
        return self.reviews
   

    def customers(self): #returns list of unique customers who reviewed the restuarant
        unique_customers=[review.customer() for review in self.reviews] #review.customer is in the review class
        return list(unique_customers)
 
    def avg_restuarant_rating(self):
        avg_rating=sum(review.rating() for review in self.reviews) / len(self.reviews)
        return avg_rating


restuarant1=Restuarant("Frangos")
restuarant2=Restuarant("The Curve")

print (restuarant1.name())
print (restuarant2.name())