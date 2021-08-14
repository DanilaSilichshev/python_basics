class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        print(f"Полное имя сотрудника: {self.surname} {self.name}")

    def get_total_income(self):
        total_income = self._income.get("wage") + self._income.get("bonus")
        print(f"Итоговый доход сотрудника составляет {total_income}")


worker_1 = Position("Николай", "Васильев", "Product-менеджер", 1000, 150)
worker_2 = Position("Илья", "Игнатенко", "Data-scientist", 1900, 300)
worker_3 = Position("Екатерина", "Игнатенко", "Python-разработчик", 1700, 200)
print(worker_1.surname, worker_2.position, worker_3.name)
worker_1.get_full_name()
worker_2.get_full_name()
worker_2.get_total_income()
worker_3.get_total_income()
