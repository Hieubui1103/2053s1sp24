from bank_account import BankAccount
account1 = BankAccount(1234567)
account2 = BankAccount(2345678, 1000)
account3 = BankAccount(3456789, 2000)

print(account1)
print(account2)
print(account3)

account1.deposit(3000)
account2.deposit(3000)
account3.deposit(3000)

account1.withdraw(5000)
account1.withdraw(1000)
account1.withdraw(5000)

print(account2.get_balance())
