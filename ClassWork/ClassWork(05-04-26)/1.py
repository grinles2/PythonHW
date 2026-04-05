class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        self.grades = []

    def __str__(self):
        return f"Студент: {self.name} {self.surname}, возраст: {self.age}"

    def show_grades(self):
        if not self.grades:
            print("Оценок нет")
        else:
            print("Оценки:", self.grades)

    def add_grade(self, grade):
        self.grades.append(grade)
        print("Успешно")


class Car:
    def __init__(self, brand, model, speed, year):
        self.brand = brand
        self.model = model
        self.speed = speed
        self.year = year

    def __str__(self):
        return f"Машина: {self.brand} {self.model}, {self.year}, скорость: {self.speed} км/ч"

    def show_info(self):
        print(self)


students = [
    Student("Леонардно", "Ди Каприо", 11),
    Student("Билли", "Айлиш", 5)
]

cars = []

while True:
    print("\n1. Показать студентов")
    print("2. Добавить оценку студенту")
    print("3. Показать оценки студента")
    print("4. Добавить машину")
    print("5. Показать машины")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        for i, s in enumerate(students):
            print(f"{i}: {s}")

    elif choice == "2":
        for i, s in enumerate(students):
            print(f"{i}: {s}")
        index = int(input("Выберите студента: "))
        grade = int(input("Введите оценку: "))
        students[index].add_grade(grade)

    elif choice == "3":
        for i, s in enumerate(students):
            print(f"{i}: {s}")
        index = int(input("Выберите студента: "))
        students[index].show_grades()

    elif choice == "4":
        brand = input("Бренд: ")
        model = input("Модель: ")
        speed = int(input("Скорость: "))
        year = int(input("Год выпуска: "))
        cars.append(Car(brand, model, speed, year))
        print("Машина добавлена")

    elif choice == "5":
        if not cars:
            print("БД машин пустая или сервер не отвечает 😎 ( кодер опять кинул в гпт сеттинги бд и положил бд) ")
        else:
            for car in cars:
                car.show_info()

    elif choice == "0":
        exit()

    else:
        print("нету такой опции")