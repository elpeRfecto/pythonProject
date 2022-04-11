class Cat:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age

    def get_name(self):
        return self.name

    def get_gender(self):
        return self.gender

    def get_age(self):
        return self.age

Baron = Cat('Барон', 'мальчик', 2)
Sam = Cat('Сэм', 'мальчик', 2)

print("Имя: ", self.name)
print("Пол: ", self.gender)
print("Возраст: ", self.age, 'года(лет)')