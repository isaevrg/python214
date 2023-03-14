class Car:
    model_name = "X7 M50i"
    year_of_issue = "2021"
    manufacturer = "BMW"
    power = "530 л.с."
    color = "white"
    price = "10790000"

    def print_info(self):
        print(" Данные автомобиля ".center(40, "*"))
        print(f"Название модели: {self.model_name}\nГод выпуска: {self.year_of_issue}\n"
              f"Производитель: {self.manufacturer}\nМощность двигателя: {self.power}\n"
              f"Цвет машины: {self.color}\nЦена: {self.price}")
        print("=" * 40)

    def input_info(self, model_name, year_of_issue, manufacturer, power, color, price):
        self.model_name = model_name
        self.year_of_issue = year_of_issue
        self.manufacturer = manufacturer
        self.power = power
        self.color = color
        self.price = price

    def set_model_name(self, name):
        self.model_name = name

    def get_model_name(self):
        return self.model_name

    def set_year_of_issue(self, year_of_issue):
        self.year_of_issue = year_of_issue

    def get_year_of_issue(self):
        return self.year_of_issue


h1 = Car()
h1.print_info()
h1.set_model_name("Elantra")
h1.input_info("Elantra", "2018", "Hyundai", "129 л.с.", "red", "1360000")
h1.print_info()
print(h1.get_model_name())
h1.set_year_of_issue("2018")
print(h1.get_year_of_issue())
