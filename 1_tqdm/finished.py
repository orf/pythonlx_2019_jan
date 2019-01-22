from tqdm import tqdm
import time
import random


for i in tqdm(range(10), total=10, position=0):
    time.sleep(random.random())
    for i in tqdm([1, 2], position=1):
        time.sleep(i)
