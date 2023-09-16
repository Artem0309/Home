# class Student:
#     print("hi , student")
#     kol=0
#     def __init__(self,name,surname,htight):
#         self.name=name
#         self.surname=surname
#         self.htight=htight
#         Student.kol+=1
#     def info(self):
#         print(self.name, self.surname,self.htight)
#
# stud1=Student("Артем","Коваленко",120)
# print("студент №",stud1.kol)
# print(stud1.name)
# print(stud1.htight)
# print(stud1.surname)
# print("\n")
# stud2=Student("Aлександров","Иванов",175)
# print("студент №",stud2.kol)
# print(stud2.name)
# print(stud2.htight)
# print(stud2.surname)
# print("\n")
# stud3=Student("ala","konov",1000)
# print("студент №",stud3.kol)
# print(stud3.name)
# print(stud3.htight)
# print(stud3.surname)
# print(Student.kol)

from random import randint
class Student:
    rnd=randint(3,7)
    def __init__(self,surname="сидоров",name="Иван",age="14"):
        self.surname=surname
        self.name = name
        self.age = age
        self.progr=0
        self.happy = 50
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
    def stud_life(self):
        if self.progr<3:
            print("Радость студента низ")
            self.life=False
        elif self.progr>=3:
            print("Радость студента верх")
            self.life=True
    def everybody(self):
        print("показатель гормона радости ",self.happy)
        print("показатель гормона обучения ",self.progr)
    def rezult(self,day):
        day="день #" +str(day)+ "статистика по студенту "+ self.surname+self.name+str(self.age)
        print(day)
        print("сейчас студент выбирает ....")
        choise=randint(1,3)
        if choise==1: self.study()
        elif choise==2: self.sleep()
        else: self.relax()
        self.stud_life()
        self.everybody()

stud1=Student()
num=int(input("Ведите переодичность "))
for day in range(1,num+1):
    stud1.rezult(day)