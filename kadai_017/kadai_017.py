class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def check_adult(self):
        if self.age >= 20:
            print("大人です")
        else:
            print("大人ではありません")

user1 = Human("あ", 9)
user2 = Human("い", 19)
user3 = Human("う", 20)
user4 = Human("え", 21)
user5 = Human("お", 20)
user6 = Human("ん", 100)

user_list = [user1, user2, user3, user4, user5, user6]

for user in user_list:
    user.check_adult()