class BankAccount:
    
    balance = 0
    fees = 0
    
    def __init__(self, initial_balance=0):
        """Creates an account with the given balance."""
        self.balance = initial_balance
        self.fees = 0
        return
    
    def deposit(self, amount):
        """Deposits the amount into the account."""
        self.balance +=amount	
        return
    
    def withdraw(self, amount):
        """Withdraws the amount from the account.  
        Each withdrawal resulting in a negative balance 
        also deducts a fee of 5 dollars from the balance."""
        self.balance -=amount	
        if (self.balance<0):
            self.fees += 5
            self.balance -=5
        return
    
    def get_balance(self):
        """Returns the current balance in the account."""
        return self.balance
    
    def get_fees(self):
        """Returns the total fees ever accrued in the account."""
        return self.fees

if (False):
    my_account = BankAccount(10)
    my_account.withdraw(15)
    my_account.deposit(20)
    print my_account.get_balance(), my_account.get_fees()
else:
    my_account = BankAccount(10)
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(5)
    my_account.withdraw(15)
    my_account.deposit(20)
    my_account.withdraw(5) 
    my_account.deposit(10)
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(30)
    my_account.withdraw(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(50) 
    my_account.deposit(30)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.deposit(20)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(5)
    my_account.deposit(10)
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(10) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.deposit(30)
    my_account.withdraw(25) 
    my_account.withdraw(10)
    my_account.deposit(20)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    my_account.withdraw(15)
    my_account.deposit(10)
    my_account.withdraw(5) 
    print my_account.get_balance(), my_account.get_fees()
