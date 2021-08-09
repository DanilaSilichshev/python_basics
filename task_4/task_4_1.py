from sys import argv

script_name, productivity, hour_rate, bonus = argv

result = (float(productivity) * float(hour_rate)) + float(bonus)
print(f"Результат = {result}")
