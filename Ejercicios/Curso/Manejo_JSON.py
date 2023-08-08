import json

"""
Python  |   JSON
dict    =>  Object
list    =>  Array
tuple   =>  Array
str =>  String
int =>  Number
float   =>  Number
True    =>  true
False   =>  false
None    =>  null 
"""



#Pasar un json a str
json_str =  '{"nombre":"Samuel", "edad":18, "pais":"Colombia"}'
print(json_str)
print(type(json_str))

python_dic = json.loads(json_str)
print(python_dic)
print(type(python_dic))


# Para pasar de str a json
data = {
    "brand":"Ford",
    "model":"Muntang",
    "year":1925,
    "Owners":["Samuel", "Jefferson", "Maria", "Rosa"]
}

json_data = json.dumps(data)
print(json_data)
print(type(json_data))


data = {
    "brand": "Ford",
    "model": "Muntang",
    "year": 1925,
    "owners": ["Samuel", "Jefferson", "Maria", "Rosa"],
}

#json_data = json.dumps(data, indent=4, separators=(",", ":"))  # El ident es la identacion. La identacion es los espacios que va a tener cada linea de codigo que define la estructura del codigo
json_data = json.dumps(data, indent=4, separators=(",", ":"), sort_keys=True) # El sort_keys es para ordenar ascendentemente las llaves
print(json_data)



# Otra manera de hacer todo lo anterior

json_data = json.JSONEncoder().encode({"owners": ["Samuel", "Jefferson", "Maria", "Rosa"]})
print(json_data)

python_dic = json.JSONDecoder().decode({json_data})
print(python_dic)


class Curso():

    def __init__(self, codigo, nombre, creditos) -> None:
        self.codigo = codigo
        self.nombre = nombre
        self.creditos = creditos
    
curso_1 = Curso("9841", "Lenguaje", 4)
print(curso_1)

json_object_data = json.dumps(curso_1.__dict__) #El .__dict__ es para volverlo un diccionario
print(json_object_data)

python_dict = json.loads(json_object_data)
print(python_dict)
