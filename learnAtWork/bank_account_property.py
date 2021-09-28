class BankAccount:
    def __init__(self, account_number, account_name, balance=0):
        self._account_number = account_number
        self._account_name = account_name
        self.balance = balance                  # gọi @balance.setter

    @property
    def account_number(self):
        return self._account_number

    @property
    def account_name(self):
        return self._account_name

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, balance):
        if balance >= 0:
            self._balance = balance
        else:
            raise ValueError("Số dư phải lớn hơn 0")

    def display(self):
        print(self.account_number, self.account_name, self.balance, "₫")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
        else:
            raise ValueError(
                "Số tiền phải lớn hơn 0 và không được vượt quá số dư hiện tại")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            raise ValueError("Số tiền phải lớn hơn 0")


my_account = BankAccount(1, "Ba", 1_000_000_000_000_000_000)
my_account.deposit(1_000_000_000_000_000_000)
my_account.display()

my_account.withdraw(100_000_000)  # quá nhỏ bé 😊
my_account.display()
