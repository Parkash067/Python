#step#1
#class name should be in camel case


# class Dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def sit(self):
#         print("This dog named {name} is sitting under a tree".format(name=self.name))
#
#     def rollover(self):
#         print("This dog named {name} is rolling for a bone. Its age is {age} years\n".format(name=self.name, age=self.age))
#
# my_dog = Dog('Puppy',4) #my_dog is an instance of a class
# my_dog.sit()
# my_dog.rollover()
#
# your_dog = Dog('Tommy',2)
# my_dog.sit()
# my_dog.rollover()

#Ex9.1,9.2

# class Restaurant():
#     def __init__(self,name,type):
#         self.restaurant_name = name
#         self.cuisine_type = type
#
#     def describe_restaurant(self):
#         print("The name of this restaurant is {name} and its cuisine type is {cuisine}"
#               .format(name=self.restaurant_name,cuisine=self.cuisine_type))
#
#     def open_restaurant(self):
#         print("Restaurant is open from Monday - Friday\n")
#
#
# nawab_restaurant = Restaurant('Nawab','Rajasthani')
# print("Restaurant's Name {name}".format(name=(nawab_restaurant.restaurant_name).title()))
# print("Cooking Type {type}".format(type=nawab_restaurant.cuisine_type.title()))
# nawab_restaurant.describe_restaurant()
# nawab_restaurant.open_restaurant()
#
# lalqila_restaurant = Restaurant('LalQila','Indian')
# print("Restaurant's Name {name}".format(name=(lalqila_restaurant.restaurant_name).title()))
# print("Cooking Type {type}".format(type=lalqila_restaurant.cuisine_type.title()))
# lalqila_restaurant.describe_restaurant()
# lalqila_restaurant.open_restaurant()

# du_darya_restaurant = Restaurant('Du Darya','Chinese')
# print("Restaurant's Name {name}".format(name=(du_darya_restaurant.restaurant_name).title()))
# print("Cooking Type {type}".format(type=du_darya_restaurant.cuisine_type.title()))
# du_darya_restaurant.describe_restaurant()
# du_darya_restaurant.open_restaurant()


#Ex9.3

# class Userprofile():
#     def __init__(self,first_name,last_name,age,nic):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.nic = nic
#
#     def descibe_user(self):
#         print("User Info\n Full Name:{name}\n Age:{age}\n NIC:{nic}"
#               .format(name=self.first_name+' '+self.last_name,age=self.age,nic=self.nic))
#
#     def greetings(self):
#         print("Helo {name}".format(name=self.first_name+' '+self.last_name))
#
#
# user = Userprofile('Parkash','Kumar',25,4220170898500)
# user.descibe_user()
# user.greetings()


# class Car():
#     """A simple attempt to represent a car."""
#     def __init__(self, make, model, year):
#         """Initialize attributes to describe a car."""
#         self.make = make
#         self.model = model
#         self.year = year
#
#     def get_descriptive_name(self):
#         """Return a neatly formatted descriptive name."""
#         long_name = str(self.year) + ' ' + self.make + ' ' + self.model
#         return long_name.title()
#
# my_new_car = Car('audi', 'a4', 2016)
# print(my_new_car.get_descriptive_name())


#Setting a Default Value for an Attribute

# class Car():
#     def __init__(self):
#         self.mileage=0
#
#     def updateMileage(self,mile):
#         self.mileage = mile
#
#     def incMileage(self,mile):
#         self.mileage += mile
#
# car = Car()
# print(car.mileage)
# # first method to update value of attribute through instance of class
# print("\nFirst method to update value of attribute through instance of class")
# car.mileage = 20
# print(car.mileage)
#
# #second method to update value of attribut through method
# print("\nSecond method to update value of attribute through method")
# car.updateMileage(400)
# print(car.mileage)
#
# #Third method to update value of attribut through increment
# print("\nThird method to update value of attribute through increment")
# car.incMileage(450)
# print(car.mileage)


#Ex9.4
# class Restaurant():
#     def __init__(self,name,type):
#         self.restaurant_name = name
#         self.cuisine_type = type
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print("The name of this restaurant is {name} and its cuisine type is {cuisine}"
#               .format(name=self.restaurant_name,cuisine=self.cuisine_type))
#
#     def open_restaurant(self):
#         print("Restaurant is open from Monday - Friday\n")
#
#     def set_number_served(self,served):
#         self.number_served = served
#
#     def inc_number_served(self, served):
#         self.number_served += served
#
#
# restaurant = Restaurant('Nawab','Rajasthani')
# print("Served Customers:{customers}".format(customers=restaurant.number_served))
#
# restaurant.set_number_served(100)
# print("\nServed Customers:{customers}".format(customers=restaurant.number_served))
#
# restaurant.inc_number_served(35)
# print("\nServed Customers:{customers}".format(customers=restaurant.number_served))


#Ex9.5

# class Userprofile():
#     def __init__(self,first_name,last_name,age,nic):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.nic = nic
#         self.login_attempts = 0
#
#     def descibe_user(self):
#         print("User Info\n Full Name:{name}\n Age:{age}\n NIC:{nic}"
#               .format(name=self.first_name+' '+self.last_name,age=self.age,nic=self.nic))
#
#     def greetings(self):
#         print("Helo {name}".format(name=self.first_name+' '+self.last_name))
#
#     def inc_login_attempts(self):
#         self.login_attempts += 1
#
#     def reset_login_attempts(self):
#         self.login_attempts = 0
#
#
# user = Userprofile('Parkash','Kumar',25,4220170898500)
# user.inc_login_attempts()
# user.inc_login_attempts()
# user.inc_login_attempts()
#
# print("Total Login attempts {attempts}".format(attempts=user.login_attempts))
#
# user.reset_login_attempts()
# print("Login attempts {attempts}".format(attempts=user.login_attempts))


