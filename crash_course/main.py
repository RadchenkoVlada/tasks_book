from restaurant import Restaurant, IceCreamStand
from user import User, Admin


if __name__ == '__main__':
    first_res = Restaurant("paprika", "italian")
    print(first_res.describe_restaurant())
    print(first_res.open_restaurant())
    second_res = Restaurant("samurai", "japanese")
    print(second_res.describe_restaurant())
    ice_cream = IceCreamStand()
    ice_cream.describe_flavours()

    print("*******************")

    u1 = User()
    u1.greet_user()
    u2 = User("vlada", "radchenko", "123445", "female")
    u2.greet_user()
    u2.describe_user()
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
