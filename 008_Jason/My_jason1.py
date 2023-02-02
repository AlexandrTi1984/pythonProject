import  json
import  _json
json_string=
#вывод как строка
data=json.loads(json_string)
print(data)
data['people'][0]['name']='Bob Smith'
#new_json=json.dumps(data, ident=2)

print(data)
#print(type(new_json))
