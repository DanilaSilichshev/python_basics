class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки.")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки модели ручки '{self.title}'.")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки модели карандаша '{self.title}'.")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки модели маркера '{self.title}'.")


pen = Pen("Гелевая")
pencil = Pencil("Цветной")
handle = Handle("Акриловый")
pen.draw()
pencil.draw()
handle.draw()
