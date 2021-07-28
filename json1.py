import json

x = '{"name":"Sandeep", "age":36, "Loc": "Noida"}'

y = json.loads(x)
print(y)
print(y["name"])
