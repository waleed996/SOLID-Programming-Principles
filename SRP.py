
# SOLID Programming Principle Examples




# Single Responsibility Principle



# Violation of SRP

class Account:
   """Demo bank account class"""

    def __init__(self, account_no: str):
        self.account_no = account_no

    # Responsibility 1 : Get Account Data.
    def get_account_number(self):
        """Get account number"""
        return self.account_no

    def get_account_balance(self):
        pass


    # Responsibility 2 : Database Save Operation
    def save(self):
        """Save account number into DB"""
        pass


# The above Account class has two responsibilities, getting account
# number (Plus there could be other non db account class behavior methods)
# And the second save operation which is a DB responsibility
























# Non Violation of SRP in the above example

# Solution: Apply the Facade pattern

class AccountDB:
    """Account DB management class"""

    def get_account_number(self, _id):
        """Get account number from db"""
        pass

    def account_save(self, obj):
        """Save the account number in db"""
        pass



class Account:
    """Demo bank account class"""

    def __init__(self, account_no: str):
        self.account_no = account_no
        self._db = AccountDB()


    def get(self, _id):
        """get account number"""

        return self._db.get_account_number(_id=_id)


    def save(self):
        """account save"""
        self._db.account_save(obj=self)


# Separate the Database Operation class from the Account class







