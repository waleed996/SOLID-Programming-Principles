# SOLID Programming Principle Examples




# Dependency Inversion Principle

# a. High Level modules should not depend on low level modules. BOTH SHOULD DEPEND ON ABSTRACTIONS.

# b. Abstractions should not depend on details. Details should depend on Abstractions.


# Violation of DIP


class BackendDeveloper:
    """This is a low level module"""

    @staticmethod
    def python():
        print("Writing python code.")


class FrontendDeveloper:
    """This is a low level module"""

    @staticmethod
    def javascript():
        print("Writing javascript code.")


class Project:
    """This is a high level module"""

    def __init__(self):
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()


    def develop(self):
        self.backend.python()
        self.frontend.javascript()

        return "Develop Project"

project = Project()
print(project.develop())

# We can see that the high level module Project depends on the low level
# modules BackendDeveloper and FrontendDeveloper, which violates DIP.


# We will introduce an abstract module to solve this.
























# Solution



class BackendDeveloper:
    """This is a low level module"""

    @staticmethod
    def python():
        print("Writing python code.")


class FrontendDeveloper:
    """This is a low level module"""

    @staticmethod
    def javascript():
        print("Writing javascript code.")



# THE ABSTRACTION

class Developers:
    """An abstract module"""

    def __init__(self):

        # Now the low level module depends on the Developers abstraction
        self.backend = BackendDeveloper()
        self.frontend = FrontendDeveloper()


    def develop(self):
        self.backend.python()
        self.frontend.javascript()




class Project:
    """This is a high level module"""

    def __init__(self):

        # By doing this, the high level module depends on the
        # Abstraction, instead of the low level modules
        self.developers = Developers()


    def develop(self):
        self.backend.python()
        self.frontend.javascript()

        return "Develop Project"



project = Project()
print(project.develop())




