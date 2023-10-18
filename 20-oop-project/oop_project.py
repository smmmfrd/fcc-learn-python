from bank_accounts import *

Sam = InterestRewardsAcct(1000, "Sam")
Dave = BankAccount(2000, "Dave")

Sam.printBalance()
Dave.printBalance()

Dave.deposit(500)

# Errors
Dave.withdraw(3000)

Dave.withdraw(30)

# Errors
Dave.transfer(10000, Sam)

Dave.transfer(100, Sam)

Blaze = SavingsAccount(1000, "Blaze")

Blaze.printBalance()

# It inherits from interest account, so 5% is added.
Blaze.deposit(100)

Blaze.transfer(10000, Sam)
Blaze.transfer(1000, Sam)
