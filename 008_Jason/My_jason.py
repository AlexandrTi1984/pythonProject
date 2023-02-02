import json
#только двойные кавычки

with open ('sample2.json','r',encoding='UTF8') as file:
    data=json.load(file)
    print(data)
    print(type(data))
for person in data['people']:
    if person['has_licence']==False:
        data['people'].remove(person)

with open ('sample2-copy.json','w',encoding='UTF8') as file:
    json.dump(data,file,indent=2)  #indent=2 в виде дерева, без него в одну строку. dump - преобразование в файл json





