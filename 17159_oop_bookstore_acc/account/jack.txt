class Account:
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            with open(filepath) as file:
                self.balance = int(file.read())
        except ValueError:
            self.balance = 0

    def withdraw(self, ammount):
        self.balance -= ammount

    def deposit(self, ammount):
        self.balance += ammount

    def commit(self):
        with open(self.filepath, 'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    def __init__(self, filepath, fee):
        self.fee = fee
        Account.__init__(self, filepath)
    
    def transfer(self, ammount):
        self.balance = self.balance - ammount - self.fee

#acc1 = Account('account/balance.txt')
#print(acc1.balance)
#acc1.withdraw(50)
#print(acc1.balance)
#acc1.deposit(1030)
#print(acc1.balance)
#acc1.commit()
ck1 = Checking('account/balance.txt', 2)
print(ck1.balance)
ck1.transfer(100)
print(ck1.balance)
