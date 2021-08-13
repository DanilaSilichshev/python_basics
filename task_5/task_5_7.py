import json

descriptive_list, firm_avg, avg_for_all_firms = list(), dict(), {"average_profit": 0}
with open("test_7_1.txt") as test_file:
    firms_quantity_for_avg, firms_profits_sum_for_avg = 0, 0
    for line in test_file:
        line = line.split()
        firm_avg[line[0]] = float(line[2]) - float(line[3])
        firms_quantity_for_avg = firms_quantity_for_avg + 1 if float(line[2]) - float(
            line[3]) > 0 else firms_quantity_for_avg
        firms_profits_sum_for_avg = firms_profits_sum_for_avg + float(line[2]) - float(
            line[3]) if float(line[2]) - float(
            line[3]) > 0 else firms_profits_sum_for_avg
    avg_for_all_firms["average_profit"] = firms_profits_sum_for_avg / firms_quantity_for_avg
    descriptive_list = [firm_avg, avg_for_all_firms]
    print(descriptive_list)

with open("test_7_2.json", "w") as write_f:
    json.dump(descriptive_list, write_f)
