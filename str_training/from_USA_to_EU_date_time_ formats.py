import os

# example: 01-05-13291593.txt -> 05-01-13291593.txt
path = "/Users/vladaradchenko/Desktop/untitled_folder"
files = os.listdir(path)
os.chdir(path)
for filename in files:  # list of str
    if filename.endswith('.txt'):
        month = filename[0:2]
        day = filename[3:5]
        result = day + filename[2] + month + filename[5:]

        # renaming real files by path
        os.rename(filename, result)
        # print(result)
