# try:
#     file = open("files/file.txt", "a")
#     try:
#         file.write("hello world\n")
#         print("file is changed")
#     except Exception as error_write:
#         print(error_write)
#     finally:
#         file.close()
# except Exception as error_open:
#     print(error_open)

# with open("files/file.txt", "a") as file:
#     print("\nDavid", file=file)

# Read only:
File = "files/file.txt"

with open(File, "r") as file:
    for line in file:
        print(line, end="")

with open(File, "r") as file:
    files = file.readline()
    string_count = 1
    while files:
        print('String', string_count, '=', files, end="")
        files = file.readline()
        string_count += 1

with open(File, "r") as file:
    files = file.read()
    print(files)

    # string type

with open(File, "r") as file:
    files = file.readlines()
    string_count = 1
    for f in files:
        print('String', string_count, '=', f, end="")
        string_count += 1
