import random

class User:
    def __init__(self, age: int):
        self.age = age
        self.chance_of_defect = False

    def chance_main(self):  # метод для расчета шанса недуга
        if self.age >= 55:
            chance_value = random.randint(1, 2)  # расчет шанса
            if chance_value == 1:
                self.chance_of_defect = True
            else:
                self.chance_of_defect = False
        else:
            self.chance_of_defect = False
        return self.chance_of_defect