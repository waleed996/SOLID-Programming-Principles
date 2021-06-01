# SOLID Programming Principle Examples




# Liskov Substitution Principle

# Child Class Object can be passed in place of the Parent Class Object



# Violation of LSP
class Vehicle:
    """Demo vehicle class"""

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


    def get_name(self):
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self):
        """Get vehicle speed"""
        return f"The vehicle name {self.speed}"


class VehicleWithoutEngine(Vehicle):

    def start_moving(self):
        pass


class VehicleWithEngine(Vehicle):

    def engine(self):
        pass

    def start_engine(self):
        pass


class Car(VehicleWithEngine):

    def start_engine(self):
        pass


class Bicycle(VehicleWithoutEngine):

    def start_moving(self):
        pass




class LSPTestViolation:

    # Vehicle passed can be Bicycle or Car
    def run_vehicle(vehicle):

        if isinstance(vehicle, Bicycle):
            # Logic for bicycle
            vehicle.start_moving()
            pass

        elif isinstance(vehicle, Car):
            # Logic for car
            vehicle.start_engine()
            pass

        else:

            pass


# We will have to check if the object passed to our function is an instance of
# VehicleWithEngine or VehicleWithoutEngine class and structure our logic
# accordingly. We donot want to do this. In case there is another subtype
# we will have to refactor the function which will in turn violate
# OCP open close priciple.















# Solution

class Vehicle:
    """Demo vehicle class"""

    def __init__(self, name, speed):
        self.name = name
        self.speed = speed


    def get_name(self):
        """Get vehicle name"""
        return f"The vehicle name {self.name}"

    def get_speed(self):
        """Get vehicle speed"""
        return f"The vehicle name {self.speed}"

    def engine(self):
        """vehicle engine"""
        pass

    def drive_vehicle(self):
        """vehicle engine start"""
        self.engine()


class Car(Vehicle):
    """Demo Car vehicle class"""

    def drive_vehicle(self):
        pass


class Bicycle(Vehicle):
    """Demo Biclycle class"""

    def drive_vehicle(self):
        pass


class LSPTestNonViolation:

    # Vehicle passed can be Bicycle or Car
    def run_vehicle(vehicle):

        # Does not matter which vehicle is passed
        vehicle.drive_vehicle()







