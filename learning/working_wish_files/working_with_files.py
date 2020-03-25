# try:
#     file = open("c:/users/ikriatov/file.txt", "a")
#     try:
#         file.write("hello world\n")
#         print("file is changed")
#     except Exception as error_write:
#         print(error_write)
#     finally:
#         file.close()
# except Exception as error_open:
#     print(error_open)

# with open("c:/users/ikriatov/file.txt", "a") as file:
#     print("\nDavid", file=file)

# Read only:

with open("c:/users/ikriatov/file.txt", "r") as file:
    for line in file:
        print(line, end="")

with open("c:/users/ikriatov/file.txt", "r") as file:
    files = file.readline()
    string_count = 1
    while files:
        print('String', string_count, '=', files, end="")
        files = file.readline()
        string_count += 1

with open("c:/users/ikriatov/file.txt", "r") as file:
    files = file.read()
    print(files)

    # string type

with open("c:/users/ikriatov/file.txt", "r") as file:
    files = file.readlines()
    string_count = 1
    for file in files:
        print('String', string_count, '=', file, end="")
        string_count += 1

    # list type