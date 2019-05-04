"""
Task from "PYTHON CRASH COURSE" by Eric Matthes
Chapter 9 - Classes

9-1. Restaurant: Make a class called Restaurant.
The __init__() method for Restaurant should store two attributes:
a restaurant_name and a cuisine_type.
 Make a method called describe_restaurant() that prints these two pieces of
information, and a method called open_restaurant() that prints a message indicating that the restaurant is open.
Make an instance called restaurant from your class. Print the two attributes individually, and then call both methods.

9-2. Three Restaurants: Start with your class from Exercise 9-1. Create three different instances from the class, and
call describe_restaurant() for each instance.

9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a
default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant
has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. Call this
method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of
business.


9-6. Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that
inherits from the Restaurant class you wrote in Exercise 9-1 (page 166) or Exercise 9-4 (page 171). Either version of
the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream
flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

"""


class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, name="Uno", cuisine_type="italian"):
        """Initialize name and type attributes."""
        self.name = name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Prints a message indicating that the restaurant is open"""
        print("The restaurant is called", self.name.title() + ".")
        print("The restaurant serves", self.cuisine_type, "cuisine.")

    def open_restaurant(self):
        print("The restaurant ", self.name.title(), "is opened!")

    def set_number_served(self, customers):
        """lets you set the number of customers that have been served"""
        self.number_served = customers

    def increment_number_served(self, customers):
        """increment the number of customers who’ve been served"""
        self.number_served += customers
        print("The number of customers the restaurant has served", self.number_served, "in Wednesday")


class IceCreamStand(Restaurant):
    def __init__(self, name="Uno", cuisine_type="italian"):
        super().__init__(name, cuisine_type)
        self.flavours = ["cherry", "chocolate", "vanilla", "grape", "halva"]

    def describe_flavours(self):
        print("Here are types of ice cream " + str(self.flavours) + "\n" + "in the ice-cream-stand")


if __name__ == '__main__':
    first_res = Restaurant("paprika", "italian")
    print(first_res.describe_restaurant())
    print(first_res.open_restaurant())
    second_res = Restaurant("samurai", "japanese")
    print(second_res.describe_restaurant())
    print(second_res.open_restaurant())
    restaurant = Restaurant("My rest", "ukr")
    print("The number of customers the restaurant has served", restaurant.number_served)
    restaurant.number_served = 5
    print("The number of customers the restaurant has served", restaurant.number_served)
    restaurant.set_number_served(56)
    print("The number of customers the restaurant has served", restaurant.number_served)
    restaurant.increment_number_served(4)
    print("*******************")
    ice_cream = IceCreamStand()
    ice_cream.describe_flavours()
    #
