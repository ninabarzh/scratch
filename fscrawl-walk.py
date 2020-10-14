import os

for (dirpath, dirnames, filenames) in os.walk('.'):
    for f in filenames:
        print('File: ', os.path.join(dirpath, f))
    for d in dirnames:
        print('Directory: ', os.path.join(dirpath, d))

