class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def check_adult(self):
        if self.age >= 20:
            print("大人です")
        else:
            print("大人ではありません")

user_names = ["あ", "い", "う", "え", "お", "ん"]
user_ages = [2, 12, 22, 32, 42, 99]

for i in range(0,5):
    user = Human(user_names[i], user_ages[i])
    user.check_adult()