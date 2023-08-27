from review import Review

class Customer:
    customers=[] #declaring a variable to hold the customers
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.customers.append(self) #appending each created instance to the list

        self.reviews=[] # used to store each customers review
    def given_name(self): #getter method used to retrieve the name
        return self.first_name
    def family_name(self):
        return self.last_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod
    def all(cls): #used to refer to the class itself and returns  a list of all customer instances
        return cls.customers
    
    def restuarants(self): #list of restuarants reviewed 
        restuarants_reviewed=[review.restuarant() for review in self.reviews]
        return list(restuarants_reviewed)
    
    def add_review(self,restuarant_name,rating):
        new_review=Review(self,restuarant_name,rating) #creating a new instance of a review 
        self.reviews.append(new_review) #adding the new review to the review list 

    def num_reviews(self): # return the total number of reviews by checking the length
        return len(self.reviews)

   

    @classmethod #decorator for class method
    def find_by_name(cls,name):
        for customer in cls.customers: #looping through the list of customers 
            if customer.full_name() == name:
              return customer
    
    def find_all_by_given_name(cls,name): #returning a list of customers if the given name matches the name
       return [customer for customer in cls.customers if customer.given_name() == name]


#testing 
customer1 = Customer("Judy", "sigilai")
customer2 = Customer("Brian", "Kip")

print(customer1.full_name())  
print(customer2.full_name())
print(customer2.given_name())
print(customer2.family_name())
print(Customer.all()) #its a class method


