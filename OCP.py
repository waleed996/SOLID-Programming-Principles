
# SOLID Programming Principle Examples




# Open/Close Princle: Software Classes, Funtion and Modules are

# OPEN FOR EXTENSION
# but
# CLOSED FOR MODIFICATION



# Violation of OCP


class Discount:
    """Demo customer discount class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price


    def give_discount(self):
        """Discount Method"""

        if self.customer == "normal":
            return self.price * 0.2
        elif self.customer == "vip":
            return self.price * 0.4


# The class and the method needs to be modified when
# there is a new category of customer like super vip customer
# like so



class Discount:
    """Demo customer discount class"""

    def __init__(self, customer, price):
        self.customer = customer
        self.price = price


    def give_discount(self):
        """Discount Method"""

        if self.customer == "normal":
            return self.price * 0.2
        elif self.customer == "vip":
            return self.price * 0.4
        elif self.customer = "supervip" # THIS NEEDS TO BE ADDED
            return self.price * 0.8
























# Solution

class Discount:
    """Demo customer discount class"""

    def __init__(self):
        self.customer = customer
        self.price = price

    def get_discount(self):
        """Get discount method"""
        return self.price * 0.2

class VIPDiscount(Discount):
    """Demo VIP customer discount"""

    def get_discount(self):
        """get vip discount"""
        return super().get_discount() * 0.2

class SuperVIPDiscount(Discount):
    """Demo super vip discount"""

    def get_discount(self):
        """get super vip discount"""
        return super().get_discount() * 0.4


