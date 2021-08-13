with open("test_2.txt") as test_file:
    lines_len = 0
    for line in test_file:
        lines_len += 1
        print(f"В {lines_len} строке {len(line.split())} слов")
    print(f"Общее число симвовов: {lines_len}")
