file_name = "C:/users/ikriatov/new_new_file1.txt"
names_list = list()

counts = int(input("Введите количество имён в списке: "))

for count in range(counts):
    name = input(f"Введите имя {count + 1}: ")
    names_list.append(name)

print(names_list)

with open(file_name, "a") as file:
    for name in names_list:
        if name == names_list[-1]:
            print(name, file=file, end="")
        else:
            print(name, file=file, end="\n")

with open(file_name, "r") as file:
    lines = file.readlines()
    for line in lines:
        print(line)