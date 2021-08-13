mini_translator = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}
file_for_read = open("test_4_1.txt", "r")
all_lines = file_for_read.readlines()
file_for_write = open("test_4_2.txt", "w")
for line in all_lines:
    new_line = line.replace(line.split()[0], mini_translator[line.split()[0]])
    file_for_write.write(new_line)
file_for_write.close()
file_for_read.close()
