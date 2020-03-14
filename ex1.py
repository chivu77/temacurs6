import re
fis=open("fisier.txt","r")
s1=fis.read()
print(s1)
s1=re.split('; |,|\.|,|\ |, |\,|\n',s1)
print(s1)
my_dict={}
for i in range(len(s1)-1):
    if s1[i] not in '.,;:/?!':
        counter = s1.count(s1[i])
        my_dict[s1[i]]=counter
print (my_dict)   