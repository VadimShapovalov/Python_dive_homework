class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name =}, {self.age =}'


class Dog(Animal):

    def __init__(self, name, age, breed, owner):
        self.breed = breed
        self.owner = owner
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name =}, {self.age =}, {self.breed =}, {self.owner =}'


class Bird(Animal):
    def __init__(self, name, age, type_, origin):
        self.type_ = type_
        self.origin = origin
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name =}, {self.age =}, {self.type_ =}, {self.origin =}'


class Fish(Animal):
    def __init__(self, name, age, habitat, size):
        self.habitat = habitat
        self.size = size
        super().__init__(name, age)

    def __str__(self):
        return f'{self.name =}, {self.age =}, {self.habitat =}, {self.size =} см'


class ZooFactory:

    def creation_animal(self):
        print('Введите цифру обозначающую тип животного:\n1. Собака \n2. Птица \n3. Рыба')
        kind = input()
        name = input('Введите имя: ')
        age = int(input('Введите возраст:'))
        if kind == '1':
            breed = input('Введите породу собаки:')
            owner = input('Введите имя хозяина:')
            dog1 = Dog(name, age, breed, owner)
            return dog1
        elif kind == '2':
            type_n = input('Введите цифру "1" если птица перелетная или цифру "2", если зимующая:')
            if type_n == '1':
                type_ = 'перелетная'
            if type_n == '2':
                type_ = 'зимующая'
            origin = input('Введите страну происхождения:')
            bird1 = Bird(name, age, type_, origin)
            return bird1
        if kind == '3':
            habitat_n = input('Введите цифру "1", если раба морская, или цифру "2", если пресноводная:')
            if habitat_n == '1':
                habitat = 'морская'
            if habitat_n == '2':
                habitat = 'пресноводная'
            size = input('Введите размер рыбы в сантиметрах:')
            fish1 = Fish(name, age, habitat, size)
            return fish1


if __name__ == '__main__':
    z_f = ZooFactory()
    animal_1 = z_f.creation_animal()
    print(f'{animal_1}')