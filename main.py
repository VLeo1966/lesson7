from zoo import Zoo, Bird, Mammal, Reptile, ZooKeeper, Veterinarian

# Создание экземпляра Zoo
zoo = Zoo()

# Создание животных
bird = Bird("Попугай", 2)
mammal = Mammal("Лев", 5)
reptile = Reptile("Змея", 3)

# Создание сотрудников
zoo_keeper = ZooKeeper("Алиса")
veterinarian = Veterinarian("Доктор Смит")

# Добавление животных и сотрудников в зоопарк
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zoo.add_staff(zoo_keeper)
zoo.add_staff(veterinarian)

# Вызов методов сотрудников
zoo_keeper.feed_animal(bird)
veterinarian.heal_animal(mammal)

# Вызов метода make_sound для всех животных
for animal in zoo.animals:
    animal.make_sound()

# Сохранение данных зоопарка в файл
zoo.save_to_file("zoo_data.pkl")

# Создание нового зоопарка и загрузка данных из файла
new_zoo = Zoo.load_from_file("zoo_data.pkl")

for animal in new_zoo.animals:
    print(f"Animal: {animal.name}, Age: {animal.age}")

for staff in new_zoo.staff:
    print(f"Staff: {staff.name}")
