import json
import operator
with open('data.json') as f:
    data=json.load(f)
print(data)
sorted_x = sorted(data.items(), key=operator.itemgetter(1))
print(sorted_x)
for i in range(len(sorted_x)):
    if i<10:
        print(sorted_x[i])
    