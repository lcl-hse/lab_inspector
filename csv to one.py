import pandas as pd

with open('data.csv') as f:
    df1 = pd.read_csv(f)

with open('data2.csv') as f:
    df2 = pd.read_csv(f)

result = pd.concat([df1, df2])
# result.drop_duplicates(subset=['name'])
result = result.values.tolist()

new_result = []
names = []

for item in result:
    name = item[0]
    if name not in names:
        new_result.append(item)
        names.append(name)


tw = '\n'.join([','.join([str(i) for i in x]) for x in new_result])

with open('rdata.csv', 'w') as f:
    f.write(tw)
