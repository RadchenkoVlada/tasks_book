"""
Task from "PYTHON CRASH COURSE" by Eric Matthes
Chapter 9 - Classes

9-3. Users: Make a class called User. Create two attributes called first_name and last_name, and then create several
other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary
of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user.
Create several instances representing different users, and call both methods for each user.

9-4. Number Served: Start with your program from Exercise 9-1 (page 166). Add an attribute called number_served with a
default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant
has served, and then change this value and print it again.
Add a method called set_number_served() that lets you set the number of customers that have been served. Call this
method with a new number and print the value again.
Add a method called increment_number_served() that lets you increment the number of customers who’ve been served.
Call this method with any number you like that could represent how many customers were served in, say, a day of
business.

9-5. Login
Attempts: Add an attribute called login_attempts to your User class from Exercise 9-3 (page 166). Write a
method called increment_ login_attempts() that increments the value of login_attempts by 1. Write another method called
reset_login_attempts() that resets the value of login_ attempts to 0.
Make an instance of the User class and call increment_login_attempts() several times. Print the value of login_attempts
to make sure it was incremented properly, and then call reset_login_attempts(). Print login_attempts again to make sure
it was reset to 0

9-7. Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you
wrote in Exercise 9-3 (page 166)
or Exercise 9-5 (page 171). Add an attribute, privileges, that stores a list
of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges()
that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

9-8. Privileges: Write a separate Privileges class. The class should have one attribute, privileges, that stores a list
of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as
an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

"""
import re


class User:
    def __init__(self, fist_name="Anna", last_name="Timchenko", tel_number="0678234672", sex="female"):
        self.first_name = fist_name
        self.last_name = last_name
        self.tel_number = tel_number
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        """Prints a summary of the user’s information"""
        print("User’s name is ", self.first_name.title())
        print("User’s last name is", self.last_name.title())
        print("User’s telephone number is", self.tel_number)
        print("User’s sex is", self.sex)

    def greet_user(self):
        """prints a personalized greeting to the user"""
        print("Hello", self.first_name.title(), self.last_name.title() + "!")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print("Now login attempts = ", self.login_attempts)

    def reset_login_attempts(self):
        self.login_attempts = 0
        print("Reset, now login attempts = ", self.login_attempts)

    def valid_tel(self):
        correct_number = re.match("^0*[0-9]{10}$", self.tel_number)
        if correct_number is None:
            return False
        else:
            return correct_number.group(0)


class Admin(User):
    def __init__(self, fist_name, last_name, tel_number, sex):
        super().__init__(fist_name, last_name, tel_number, sex)
        self.privileges = Privileges()


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("These privileges can do admin: " + str(self.privileges))


if __name__ == '__main__':

    u1 = User()
    u1.greet_user()
    u2 = User("vlada", "radchenko", "123445", "female")
    u2.greet_user()
    u2.describe_user()
    u3 = User("arnold", "ivanov", "3437273", "male")
    u3.tel_number = "1111111"
    u3.describe_user()
    print(u3.valid_tel())
    u4 = User()
    print(u4.valid_tel())
    new_user = User("Peter", "English")
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.increment_login_attempts()
    new_user.reset_login_attempts()
    print("*******************")
    user = Admin("Vasya", "Ivanov", "0507678712", "male")
    user.privileges.show_privileges()
    #
