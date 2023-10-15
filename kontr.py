class Bankacc:
    def __init__(self, name):
        self.name = name
        self.balance = 0
        self.history = []

    def deposit(self, amount):
        self.balance += amount
        self.history.append(f"Deposited: {amount}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Withdrew: {amount}")
        else:
            print("\033[91mError: Insufficient funds\033[0m")

    def view_history(self):
        print(f"\nTransaction history for {self.name}:")
        for entry in self.history:
            print(entry)

    def view_balance(self):
        print(f"\nCurrent balance for {self.name}: {self.balance}")

    def transfer(self, recipient, amount):
        if amount <= self.balance:
            self.balance -= amount
            self.history.append(f"Transferred {amount} to {recipient.name}")
            recipient.deposit(amount)
        else:
            print("\033[91mError: Insufficient funds for transfer\033[0m")
def main():
    user_account = Bankacc("John Doe")
    recipient_account = Bankacc("Jane Doe")

    while True:
        print("\n1 - Пополнить баланс")
        print("2 - Снять средства")
        print("3 - Просмотреть историю")
        print("4 - Просмотреть баланс")
        print("5 - Перевод средств")
        print("0 - Выйти")

        choice = input("Ваш выбор: ")

        if choice == "1":
            amount = float(input("Введите сумму для пополнения: "))
            user_account.deposit(amount)

        elif choice == "2":
            amount = float(input("Введите сумму для снятия: "))
            user_account.withdraw(amount)

        elif choice == "3":
            user_account.view_history()

        elif choice == "4":
            user_account.view_balance()

        elif choice == "5":
            amount = float(input("Введите сумму для перевода: "))
            user_account.transfer(recipient_account, amount)

        elif choice == "0":
            break

        else:
            print("\033[91mError: Неверный выбор\033[0m")

if __name__ == "__main__":
    main()
