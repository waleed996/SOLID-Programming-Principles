# SOLID Programming Principle Examples




# Interface Segregation Principle

# A client should not be forced to implement an interface that it does not use



# Violation of ISP

class Shape:
    """Demo shape class"""

    @abstractmethod
    def draw_circle(self):
        pass

    @abstractmethod
    def draw_square(self):
        pass


class Circle(Shape):
    """Demo Circle class"""

    def draw_circle(self):
        pass

    # Violation of ISP
    def draw_square(self):
        pass








# Solution

class Shape:
    """Demo shape class"""

    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    """Demo Circle class"""

    def draw(self):
        # Draw circle
        pass


class Square(Shape):
    """Demo Square class"""

    def draw(self):
        # Draw square
        pass



# By changing the the Shape interface in the above way the
# the classes implementing the Shape interface do not violate ISP.



