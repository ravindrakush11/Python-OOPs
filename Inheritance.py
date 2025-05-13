
# Inheritance

class Parent:
    def greet(self):
        print("Hello form Parent!")

class Child(Parent):
    def say_hi(self):
        print("Hi from Child!")
c = Child()
c.greet()
c.say_hi()


# ----------------


# Multilevel Inheritance
class A:
    def showA(self):
        print("A")

class B(A):
    def showB(self):
        print("B")

class C(B):
    def showC(self):
        print("C")

obj = C()
obj.showA()
obj.showB()
obj.showC()


# ----------------


class A:
    def __init__(self):
        print("A__init__")

    def name(self):
        print("name")

class B(A):
    def __init__(self):
        print("B__init__")

class C(B):
    def __init__(self):
        print("C__init__")

a = A()
b = B()
c = C()

# ----------------


# Super method calling

# The super() function returns an object that represents the parent class.


class A:
    def __init__(self):
        print("A__init__")

class B(A):
    def __init__(self):
        print("B__init__")
        super().__init__()

class C(B):
    def __init__(self):
        print("C__init__")
        super().__init__()


print(C.__mro__)
c = C()


# ----------------


class User:
    def __init__(self, username):
        self._username = username

class Admin(User):
    def __init__(self, username, level):

        # Call the parent class constructor  to set _username
        super().__init__(username)

        # Private attribute (name mangled to _Admin_admin_level)
        self.__admin_level = level

    def get_admin_info(self):
        # Return a formatted string with protected adn private attributes
        return f"{self._username} (Admin Level: {self.__admin_level})"

# Creating an instance of Admin with username
a = Admin("admin123", 5)

# Call the method to get admin info and print the result
print(a.get_admin_info())
