class Student:
    def __init__(self):
        self.name = "Sanya"
        self.surname = "Joystic"
        self.age = 15
        self.dyplom = [9, 10, 8, 7, 11, 2, 2]
        self.dyplom1 = sum(self.dyplom) / len(self.dyplom)

class дипломстудентаосбб:
    def diplomatic(self):
        if self.dyplom1 > 9 and 10> self.dyplom1:
            print("Ю ар вері смарт конградилейшнс")
        if self.dyplom1 < 8:
            print("ай сінк ітс окей")
        if self.dyplom1 > 7:
            print("вері бед")


    def method(self):
        print("про студента і про його диплом")

class recruit(Student, дипломстудентаосбб):
    def pr(self):
        self.method()
        print(f"{self.name} {self.surname}")
        print(f"age = {self.age}")
        print(f"marks = {self.dyplom}")
        print(f"marks = {self.dyplom1}")
        self.diplomatic()

recruit1 = recruit()
recruit1.pr()