class Wallet:
    def __init__(self):
        self.money = 0

    def add_money(self, amount):
        self.money += amount

    def withdraw(self, amount):
        if amount <= self.money:
            self.money -= amount
        else:
            print("Fonduri insuficiente")

# Creăm un obiect Wallet
my_wallet = Wallet()
my_wallet.add_money(100)
my_wallet.add_money(50)

# Afișăm suma din portofel
print(my_wallet.money)

class User:
    def __init__(self, name):
        self.name = name
        self.wallet = Wallet()

user = User("Mihai")
user.wallet.add_money(100)
print(user.wallet.money)
print(user.name)
user.wallet.withdraw(20)
print(user.wallet.money)
