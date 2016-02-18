
class BankAccount:

    def __init__(self, starting_balance: int)->None:
        self.balance = int_or_zero(starting_balance)

    def __str__(self)->str:
        return 'Balance: {}'.format(self.balance)

    def set_balance(self, new_balance)->None:
        self.balance = int_or_zero(new_balance)

    def get_balance(self)->int:
        return self.balance

    def deposit(self, amount: int)->None:
        self.balance += int_or_zero(amount)

    def withdraw(self, amount: int)->None:
        self.balance -= int_or_zero(amount)


def int_or_zero(presumed_int: any)->int:
    try:
        presumed_int = int(presumed_int)
        return presumed_int
    except ValueError:
        return 0


def main()->None:

    test_account = BankAccount(100)

    test_account.withdraw(50)
    print(test_account)

    test_account.deposit(100)
    print(test_account)

if __name__ == '__main__':
    main()