with open("test_3.txt") as test_file:
    small_salaries_workers, all_salaries = [], []
    for line in test_file:
        line = line.split(": ")
        if float(line[1]) < 20000:
            line[0] = line[0]
            small_salaries_workers.append(line[0])
        all_salaries.append(float(line[1]))
    small_salaries_workers = ", ".join(small_salaries_workers)
    print(f"Сотрудники с зп < 20000: {small_salaries_workers}; "
          f"средняя величина дохода: {sum(all_salaries) / len(all_salaries)}")
