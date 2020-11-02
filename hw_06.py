class Fib():
    """Число Фибоначчи.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Проверка, что start не изменился
    8
    """

    def __init__(self, value=0):
        self.value = value

    def next(self):
        if self.value == 0:
            a = 1
            return a
        elif a == 1:
            b = 1
#            a += 1
            return self.value + a
        elif b >= 1:
          b += 1
          return self.value + b
        self.value += 1


        "*** ТВОЙ КОД ЗДЕСЬ ***"

    def __repr__(self):
        return str(self.value)

class VendingMachine:
    """Торговый автомат, продающий некоторый товар по некоторой цене.
    
    >>> v = VendingMachine('яблоко', 10)
    >>> v.vend()
    'Товара нет в наличии.'
    >>> v.restock(2)
    'Количество товара «яблоко»: 2'
    >>> v.vend()
    'Нужно дополнительно внести 10 ₽.'
    >>> v.deposit(7)
    'Доступно: 7 ₽'
    >>> v.vend()
    'Нужно дополнительно внести 3 ₽.'
    >>> v.deposit(5)
    'Доступно: 12 ₽'
    >>> v.vend()
    'Получите яблоко и сдачу 2 ₽.'
    >>> v.deposit(10)
    'Доступно: 10 ₽'
    >>> v.vend()
    'Получите яблоко.'
    >>> v.deposit(15)
    'Товара нет в наличии. Вот твои деньги — 15 ₽.'

    >>> w = VendingMachine('лимонад', 2)
    >>> w.restock(3)
    'Количество товара «лимонад»: 3'
    >>> w.restock(3)
    'Количество товара «лимонад»: 6'
    >>> w.deposit(2)
    'Доступно: 2 ₽'
    >>> w.vend()
    'Получите лимонад.'
    """
    balance = 0
    quantity = 0
    zero_balance = 0
    def __init__(self, product_name, price): # Конструктор
        self.product_name = product_name
        self.price = price
        self.balance = VendingMachine.balance
        self.quantity = VendingMachine.quantity
        self.zero_balance = VendingMachine.zero_balance

    def vend(self): # Покупаем товар
        if self.quantity == 0:
            return 'Товара нет в наличии.'
        else:
            if self.balance == self.price:
                self.balance = 0
                return 'Получите' + ' ' + self.product_name + '.'
            elif self.balance < self.price:
                return 'Нужно дополнительно внести' + ' ' + str(self.price - self.balance) + ' ₽.'
            elif self.balance > self.price:
                self.zero_balance = self.balance
                self.balance = 0
                return 'Получите ' + self.product_name + ' и сдачу ' + str(self.zero_balance - self.price) + ' ₽.'


    def restock(self, quantity): # Проверяем количество товара
        self.quantity = quantity + self.quantity
        return 'Количество товара ' + '«' + self.product_name + '»: ' + str(self.quantity)

    def deposit(self, balance):
        self.balance += balance
        return 'Доступно: ' +  str(self.balance) + ' ₽'