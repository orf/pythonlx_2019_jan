import os

cwd = os.path.normpath(os.path.join(os.getcwd(), '..'))

for directory in os.listdir(cwd):
    directory = os.path.join(cwd, directory)
    if os.path.isdir(directory):
        print(directory)
        for file in os.listdir(directory):
            print(' - ', file)
