class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created\n\tBalance = ${self.balance:.2f}")

    def printBalance(self):
        print(f"\nAccount '{self.name}': Balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("\nDeposit Complete")
        self.printBalance()

    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has ${self.balance:.2f}"
            )

    def withdraw(self, amount):
        try:
            # This method raises an error if not viable
            self.viableTransaction(amount)

            self.balance = self.balance - amount
            print("\nWithdraw complete.")
            self.printBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):
        try:
            print("\n**********\n\nBeginning Transfer... 🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\n✅ Transfer Complete\n\n**********")
        except BalanceException as error:
            print(f"\n❌ Transfer interrupted: {error}")


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nInterest Rewards Deposit Complete")
        self.printBalance()


class SavingsAccount(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        self.withdrawFee = 5

    def withdraw(self, amount):
        try:
            fullamount = amount + self.withdrawFee
            # This method raises an error if not viable
            self.viableTransaction(fullamount)

            self.balance = self.balance - fullamount
            print("\nWithdraw complete.")
            self.printBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
