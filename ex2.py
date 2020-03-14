import ex1
import json
lista=list(ex1.my_dict)
print(lista)
new_dict={}
for i in range(len(lista)):
    if ex1.my_dict[lista[i]]/len(lista)<0.1:
        new_dict[lista[i]]=ex1.my_dict[lista[i]]/len(lista)
print(new_dict)
with open('data.json','w')as f:
    json.dump(new_dict,f,indent=4)