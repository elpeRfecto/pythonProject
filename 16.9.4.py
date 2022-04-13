class Guests:
    def __init__(self, name, surname, city, status):
        self.name = name
        self.surname = surname
        self.city = city
        self.status = status

    def info(self):
        return [self.name, self.surname, self.city, self.status]

class Volonteers(Guests):
    pass

allguests = []

def add_guest():
    try:
        new_guest = int(input('Сколько гостей будет: '))
        for i in range(new_guest):
            nameOfGuest = input(f'Ведите имя гостя № {i + 1}: ')
            surnameOfGuest = input(f'Ведите фамилию гостя № {i + 1}: ')
            cityOfGuest = input(f'Ведите город гостя № {i + 1}: ')
            statusOfGuest = input(f'Ведите статус гостя № {i + 1}: ')
            allguests.append(Guests(nameOfGuest, surnameOfGuest, cityOfGuest, statusOfGuest))
    except:
        print('Упс, что-то пошло не так. Попробуйте снова.')
        add_guest()

def get_guests():
    if allguests:
        print('Список гостей:')
        for guest in allguests:
            print(f' {guest.info()[0]} {guest.info()[1]}, г. {guest.info()[2]}, статус: "{guest.info()[3]}"')
    else:
        print('Список гостей пуст')

add_guest()

print('-' * 40)

get_guests()