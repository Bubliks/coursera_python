class Value:
    def __init__(self):
        self.value = None

    def __get__(self, instance, owner):
        return self.value

    @staticmethod
    def _calculate_percent(value, percent):
        return value - value * percent

    def __set__(self, instance, value):
        self.value = self._calculate_percent(value, instance.commission)

    def __delete__(self, instance):
        pass


class Account:
    amount = Value()

    def __init__(self, commission):
        self.commission = commission


def main():
    new_account = Account(0.1)
    new_account.amount = 100

    print(new_account.amount)


if __name__ == "__main__":
    main()