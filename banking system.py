class juliHomes:
    def __init__(self, house_number, house_holder_name, initial_rent=0):
        self.house_number = account_number
        self.house_holder_name = account_holder_name
        self.balance = initial_balance
        self.transaction_history = []  # A list to store transaction history

    def deposit(self, amount):
        """Deposit money into the account"""
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited: ${amount}")
            print(f"${amount} deposited successfully. New balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Withdraw money from the account"""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.transaction_history.append(f"Withdrew: ${amount}")
                print(f"${amount} withdrawn successfully. New balance: ${self.balance}")
            else:
                print("Insufficient funds for this withdrawal.")
        else:
            print("Withdrawal amount must be positive.")

    def check_balance(self):
        """Check the account balance"""
        print(f"Account balance: ${self.balance}")

    def show_transaction_history(self):
        """Display the transaction history"""
        print("\nTransaction History:")
        if self.transaction_history:
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

    def account_details(self):
        """Display account details"""
        print(f"\nAccount Number: {self.account_number}")
        print(f"Account Holder: {self.account_holder_name}")
        print(f"Current Balance: ${self.balance}")


# Bank class to manage multiple accounts
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, account_holder_name, initial_balance=0):
        """Create a new account"""
        if account_number not in self.accounts:
            new_account = BankAccount(account_number, account_holder_name, initial_balance)
            self.accounts[account_number] = new_account
            print(f"Account created successfully for {account_holder_name} with account number {account_number}.")
        else:
            print("Account number already exists.")

    def get_account(self, account_number):
        """Retrieve an account by its number"""
        return self.accounts.get(account_number, None)


# Function to display the banking menu
def banking_menu():
    print("\n--- Welcome to Python Banking System ---")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Show Transaction History")
    print("6. Show Account Details")
    print("7. Exit")


def main():
    bank = Bank()

    while True:
        banking_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            account_number = input("Enter account number: ")
            account_holder_name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial deposit amount (default $0): ") or 0)
            bank.create_account(account_number, account_holder_name, initial_balance)

        elif choice == "2":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            else:
                print("Account not found.")

        elif choice == "3":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            else:
                print("Account not found.")

        elif choice == "4":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.check_balance()
            else:
                print("Account not found.")

        elif choice == "5":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.show_transaction_history()
            else:
                print("Account not found.")

        elif choice == "6":
            account_number = input("Enter account number: ")
            account = bank.get_account(account_number)
            if account:
                account.account_details()
            else:
                print("Account not found.")

        elif choice == "7":
            print("Thank you for using the Python Banking System!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()

