
class BankAccount:

    def __init__(self, starting_balance: int)->None:
        self.balance = starting_balance

    def __str__(self)->str:
        return 'Balance: {}'.format(self.balance)

    def set_balance(self, new_balance)->None:
        self.balance = new_balance

    def get_balance(self)->int:
        return self.balance

    def deposit(self, amount: int)->None:
        self.balance += amount

    def withdraw(self, amount: int)->None:
        self.balance -= amount


def main()->None:
    pass

if __name__ == '__main__':
    main()