class StoreProduction:
    all_products = []

    def __init__(self, title, price, quantity, vendor, EAN, productivity, product_type):
        self.title = title
        self.price = price
        self.quantity = quantity
        self.vendor = vendor
        self.EAN = EAN
        self.productivity = productivity
        self.product_type = product_type
        self.all_products.append([title, price, quantity, vendor, EAN, productivity, product_type])

    def __str__(self):
        return f"На склад доставлен {self.product_type} '{self.title}' в количестве {self.quantity} с ценой {self.price} за ед. товара"

    def receive_product(self):
        try:
            self.all_products.append([input("Введите наименование: "), float(input("Введите стоимость: ")),
                                      int(input("Введите количество: ")), input("Введите страну-производителя: "),
                                      int(input("Введите код товара: ")),
                                      float(input("Введите данные про продуктивности: ")),
                                      input("Введите тип товара: ")])
        except:
            print(f"Формат переданных данных некорректен")

    def send_product(self, place):
        return f"Товар {self.title} отправлен в {place}"


class Printer(StoreProduction):
    def __init__(self, title, price, quantity, vendor, EAN, productivity, product_type="принтер"):
        super().__init__(title, price, quantity, vendor, EAN, productivity, product_type)

    def get_print_productivity(self):
        return f"Скорость печати {self.title} составляет {self.productivity} листов за минуту"


class Scanner(StoreProduction):
    def __init__(self, title, price, quantity, vendor, EAN, productivity, product_type="сканнер"):
        super().__init__(title, price, quantity, vendor, EAN, productivity, product_type)

    def get_scan_productivity(self):
        return f"Скорость скана {self.title} составляет {self.productivity} листов за минуту"


class Copier(StoreProduction):
    def __init__(self, title, price, quantity, vendor, EAN, productivity, product_type="ксерокс"):
        super().__init__(title, price, quantity, vendor, EAN, productivity, product_type)

    def get_copy_productivity(self):
        return f"Скорость ксерокопии {self.title} составляет {self.productivity} листов за минуту"


product_1 = Printer("hp", 2000, 3, "Китай", 55484841, 8)
product_2 = Scanner("Canon", 1200, 5, "Япония", 55445352, 6)
product_3 = Copier("Xerox", 1500, 7, "США", 7785255, 5)
product_4 = StoreProduction("hp", 2200, 1, "Китай", 5553550, 10, "принтер")
print(product_4)
print(product_4.__dict__)
print(product_2.get_scan_productivity())
print(product_3.send_product("отдел транспортно-хозяйственный"))
product_1.receive_product()
print(StoreProduction.all_products)
