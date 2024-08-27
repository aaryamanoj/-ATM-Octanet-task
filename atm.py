class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount:.2f}")
            print(f"New Balance: ${self.balance:.2f}")
        else:
            print("Invalid deposit amount. Please enter a positive value.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            print(f"New Balance: ${self.balance:.2f}")
        elif amount > self.balance:
            print("Insufficient funds for this withdrawal.")
        else:
            print("Invalid withdrawal amount. Please enter a positive value.")

# Assuming we start with an initial balance of 0
c = BankAccount()

while True:
    print(" D - Deposit \t W - Withdraw \t E - Exit ")
    option = input("Enter your option: ").strip().lower()

    if option == 'd':
        try:
            amount = float(input("Enter the deposit amount: "))
            c.deposit(amount)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    elif option == 'w':
        try:
            amount = float(input("Enter the withdrawal amount: "))
            c.withdraw(amount)
        except ValueError:
            print("Invalid input. Please enter a numerical value.")
    elif option == 'e':
        print("Exiting the program.")
        break
    else:
        print("You entered an invalid option. Please try again.")
