import pickle

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        raise NotImplementedError("This method should be overridden in subclasses")

class Bird(Animal):
    def make_sound(self):
        print(f"{self.name} чирикает.")

class Mammal(Animal):
    def make_sound(self):
        print(f"{self.name} рычит.")

class Reptile(Animal):
    def make_sound(self):
        print(f"{self.name} шипит.")

class Staff:
    def __init__(self, name):
        self.name = name

class ZooKeeper(Staff):
    def feed_animal(self, animal):
        print(f"{self.name} кормит {animal.name}.")

class Veterinarian(Staff):
    def heal_animal(self, animal):
        print(f"{self.name} лечит {animal.name}.")

class Zoo:
    def __init__(self):
        self.animals = []
        self.staff = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} добавлен в зоопарк.")

    def add_staff(self, staff_member):
        self.staff.append(staff_member)
        print(f"{staff_member.name} добавлен в персонал зоопарка.")

    def save_to_file(self, filename):
        with open(filename, 'wb') as file:
            pickle.dump(self, file)
        print(f"Данные зоопарка сохранены в файл {filename}.")

    @staticmethod
    def load_from_file(filename):
        with open(filename, 'rb') as file:
            zoo = pickle.load(file)
        print(f"Данные зоопарка загружены из файла {filename}.")
        return zoo
