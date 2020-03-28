import os

# os.rmdir('renamed_files')
folders = ('files', 'renamed_files')
file_name = 'hello.txt'

print(folders)

files_index = folders.index('files')
renamed_files_index = folders.index('renamed_files')

try:
    os.mkdir(folders[files_index])
    print("Folders '{}' is created".format(folders[files_index]))
except ValueError:
    print("Folder '{}' is already created".format(folders[files_index]))
os.rename(folders[files_index], folders[renamed_files_index])
print("Folder '{}' is renamed to '{}'".format(folders[files_index], folders[renamed_files_index]))

if os.path.exists(folders[renamed_files_index]):
    print("Folder '{}' exists".format(folders[renamed_files_index]))
else:
    print(f"Folder {folders[renamed_files_index]} does not exist")

full_file_name = '{}/{}'.format(folders[renamed_files_index], file_name)

with open(full_file_name, "w") as text_file:
    text_file.write("Hello")

with open(full_file_name, "r") as text_file:
    print(f"File '{file_name}' is created: {text_file.readline()}")

os.remove(full_file_name)
print("File '{}' is deleted".format(file_name))
os.rmdir(folders[renamed_files_index])
print("Folder '{}' is deleted".format(folders[renamed_files_index]))

for index, folder in enumerate(folders):
    if os.path.exists(folder):
        print(f"Folder '{index, folder}' exists")
    else:
        print(f"Folder '{index, folder}' does not exist")