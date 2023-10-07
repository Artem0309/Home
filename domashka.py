from random import randint
class Student:
    rnd=randint(3,7)
    def __init__(self,surname="сидоров",name="Иван",age="14"):
        self.surname=surname
        self.name = name
        self.age = age
        self.progr=0
        self.happy = 50
        self.money = 0
        self.life = True
    def study(self):
        print("Время для учебы\n","="*15)
        self.progr+=Student.rnd
        self.happy-=Student.rnd
    def sleep(self):
        print("Время иди спать\n", "=" * 15)
        self.happy +=Student.rnd
    def relax(self):
        print("Время для отдыха\n", "=" * 15)
        self.progr-=Student.rnd
        self.happy+=Student.rnd
    def robota(self):
        print("Время для работы\n", "=" * 15)
        self.money += Student.rnd
        self.progr += Student.rnd
        self.happy -= Student.rnd
    def stud_life(self):
        if self.progr<4:
            print("Радость студента низ")
            self.life=False
        elif self.progr>=4:
            print("Радость студента верх")
            self.life=True
    def everybody(self):
        print("показатель гормона радости ",self.happy)
        print("показатель гормона обучения ",self.progr)
        print("показатель сколько заработал", self.money)
    def rezult(self,day):
        day="день #" +str(day)+ "статистика по студенту "+ self.surname+self.name+str(self.age)
        print(day)
        print("сейчас студент выбирает ....")
        choise=randint(1,4)
        if choise==1: self.study()
        elif choise==2: self.sleep()
        elif choise==4: self.money()
        else: self.relax()
        self.stud_life()
        self.everybody()

stud1=Student()
num=int(input("Ведите переодичность "))
for day in range(1,num+1):
    stud1.rezult(day)




