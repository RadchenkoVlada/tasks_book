import os


path = "/Users/vladaradchenko/Desktop/untitled_folder"
files = os.listdir(path)
os.chdir(path)
for filename in files:  # list of str
    if filename.endswith('.txt'):
        change = str(int(filename[5:9], base=16))
        result = filename[0:5] + change + filename[9:]
        os.rename(filename, result)
        print(result)
