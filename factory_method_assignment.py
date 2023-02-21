'''
creating
factory method 

'''
class Burger:
    def cook(self):
        return "veg burger"
    def rating(self):
        return 1


class BeefBurger:
    def cook(self):
        return "beef burger"
    def rating(self):
        return 2

class PizzaBurger:
    def cook(self):
        return "pizza burger"
    def rating(self):
        return 3

class PatatoCornBurger:
    def cook(self):
        return "patato corn burger"
    def rating(self):
        return 4

class VegBurger:
    def cook(self):
        return "veg burger"
    def rating(self):
        return 5

class NonVegBurger:
    def cook(self):
        return "non veg burger"
    def rating(self):
        return 6



class StuffedBeanBurger:
    def cook(self):
        return "stuffed bean burger"
    def rating(self):
        return 8

class SupremeVeggieBurger:
    def cook(self):
        return "supreme veggie burger"
    def rating(self):
        return 7
'''
creating factory method
'''
def Factory(product = "burger"):
    items = {
        "burger":Burger(),
        "beefburger":BeefBurger(),
        "pizzaburger":PizzaBurger(),
        "vegburger":VegBurger(),
        "nonvegburger":NonVegBurger(),
        "patatocornburger":PatatoCornBurger(),
        "supremeveggieburger":SupremeVeggieBurger(),
        "stuffedbeanburger":StuffedBeanBurger()
    }
    
    return items[product.lower()]

obj = Factory()
'''
creating list

'''

l = ["burger","beefburger","PizzaBurger","vegburger","nonvegburger",
    "patatocornburger","supremeveggieburger","stuffedbeanburger",]

for i in l:
    '''
    using for loop for iteration 
    throughtout the list
    '''
    
    print(Factory(i).cook())
    
    print("rating =",Factory(i).rating())
    
    