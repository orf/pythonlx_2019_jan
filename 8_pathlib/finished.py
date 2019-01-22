from pathlib import Path


cwd = Path.cwd().parent

for f in cwd.iterdir():
    if f.is_dir():
        print(f)
        for file in f.iterdir():
            print(' - ', file)
