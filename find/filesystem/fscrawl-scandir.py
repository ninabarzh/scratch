import os

filepaths = [f.path for f in os.scandir('.') if f.is_file()]
dirpaths = [f.path for f in os.scandir('.') if f.is_dir()]

print(filepaths)
print(dirpaths)
