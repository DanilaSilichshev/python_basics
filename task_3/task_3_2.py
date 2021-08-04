def user_data(name, surname, email, residence_city, phone, birth_year):
    print(f"Имя: {name}, фамилия: {surname}, email: {email}, город проживания: {residence_city},"
          f" телефон: {phone}, год рождения: {birth_year}")


user_data(name=input("Введите имя: "), surname=input("Введите фамилию: "), phone=input("Введите телефон: "),
          residence_city=input("Введите город проживания: "), birth_year=input("Введите год рождения: "),
          email=input("Введите email: "))
