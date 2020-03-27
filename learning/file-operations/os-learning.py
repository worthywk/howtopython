import os

# os.rmdir('renamed_files')

try:
    os.mkdir("files")
    print("Folder 'files' is created")
except Exception:
    print("Folder 'files' is already created")
os.rename('files', 'renamed_files')
print("'files' is renamed to 'renamed_files'")

if os.path.exists('renamed_files'):
    print("Folder 'renamed_files' exists")
else:
    print("Folder doesn't exist")

with open('renamed_files/hello.txt', "w") as text_file:
    text_file.write("Hello")

with open('renamed_files/hello.txt', "r") as text_file:
    print(f"File 'hello.txt' is created: {text_file.readline()}")

os.remove("./renamed_files/hello.txt")
print("File 'hello.txt' is deleted")
os.rmdir('renamed_files')
print("Folder 'renamed_files' is deleted")

for folder in ['files', 'renamed_files']:
    if os.path.exists(folder):
        print(f"Folder '{folder}' exists")
    else:
        print(f"Folder '{folder}' doesn't exist")
