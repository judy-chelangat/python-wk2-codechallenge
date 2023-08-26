# Restaurant __init__()`
# - Restaurants should be initialized with a name, as a string
#- `Restaurant name()`
# - returns the restaurant's name
#- should not be able to change after the restaurant is created
 

class Restuarant:
    def __init__(self,restuarant_name): #initialized the restuarant with a name
        self.restuarant_name=restuarant_name

    def name(self):
        return self.restuarant_name
    

restuarant1=Restuarant("Frangos")
restuarant2=Restuarant("The Curve")

print (restuarant1.name())
print (restuarant2.name())