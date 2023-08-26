class Customer:
    customers=[] #declaring a variable to hold the customers
    def __init__(self,first_name,last_name):
        self.first_name=first_name
        self.last_name=last_name
        self.customers.append(self) #appending each created instance to the list
    def given_name(self): #getter method used to retrieve the name
        return self.first_name
    def family_name(self):
        return self.last_name
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    
    @classmethod #decorator for class method
    def all(cls): #used to refer to the class itself 
        return cls.customers
    

customer1 = Customer("Judy", "sigilai")
customer2 = Customer("Brian", "Kip")

print(customer1.full_name())  
print(customer2.full_name())
print(customer2.given_name())
print(customer2.family_name())
print(Customer.all()) #its a class method