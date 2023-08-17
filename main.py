class FinancialTracker:
    def __init__(self, initial_balance):
        self.balance = initial_balance
        self.transactions = []

    def add_transaction(self, description, amount):
        self.transactions.append((description, amount))
        self.balance += amount

    def print_transactions(self):
        for desc, amount in self.transactions:
            print(f"{desc:30} {amount:10.2f}")

    def print_balance(self):
        print("Total: {:.2f}".format(self.balance))

# Başlangıç bakiyesi ile finansal takip oluştur
tracker = FinancialTracker(1000.00)

# İşlemleri ekle
tracker.add_transaction("groceries", -10.15)
tracker.add_transaction("restaurant and more foo", -15.89)
tracker.add_transaction("Transfer to Clothing", -50.00)

# İşlemleri ve toplam bakiyeyi yazdır
print("*************Food*************")
tracker.print_transactions()
tracker.print_balance()
