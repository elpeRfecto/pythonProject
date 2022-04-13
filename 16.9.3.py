class Wallet:
    def __init__(self, name, last_name, balance):
        self.name = name
        self.last_name = last_name
        self.balance = balance

    def wallet(self):
        return f'(Клиент: {self.name} {self.last_name}, Баланс: {self.balance} руб.)'

electronic_wallet = Wallet('Иван', 'Петров', '50')

print(electronic_wallet.wallet())