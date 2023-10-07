import random

class Human:
    def __init__(self, name='Александр', age=30, money=random.randint(300, 500), home=0, amount=None):
        self.name = name
        self.age = age
        self.money = money
        self.home = home
        self.amount = amount

    def earn_money(self, amount):
        self.money += amount

    def buy_house(self):
        while self.money < 500:
            print('Иди работай, у тебя не достаточно денег для покупки дома!!!')
            self.earn_money(random.randint(300, 500))
        self.home += 1
        print('Поздравляю с новым домом!')

    def infoH(self):
        print('Имя:', self.name, 'Возраст:', self.age, 'Сколько ты заработал:', self.money)

tr = Human()
tr.infoH()
print('-' * 50)
tr.buy_house()
print('-' * 50)

class House:
    def __init__(self, area, price):
        self.area = area
        self.price = price

    def final_price(self, discount=0):
        return self.price * (1 - discount / 100)


tr = Human()
tr.infoH()
print('-'*50)

house = House(area=200, price=15000)
print('Исходная цена дома:', house.final_price())

discounted_price = house.final_price(discount=10)
print('Цена дома с 10% скидкой:', discounted_price)

print('-'*50)

tr.earn_money(400)
tr.infoH()

print('-'*50)


print('-'*50)

class small_house(House):
    def __init__(self,area=40,price=5000):
        super().__init__(area,price)
    def Infov(self):
       print('площадь твоего маленького дома:',self.area,'','цена маленького дома:',self.price,)


fr=small_house()
fr.Infov()