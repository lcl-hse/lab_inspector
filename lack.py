import os
from tqdm.auto import tqdm

with open('data.txt', encoding='utf-8') as f:
    data = f.read().splitlines()

paths = [x[0] for x in [y.split('\t') for y in data]]

lacks = []

for path in tqdm(paths):
    npath = os.path.join('exam', path)
    if not os.path.exists(npath):
        lacks.append(path)

with open('lack.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lacks))