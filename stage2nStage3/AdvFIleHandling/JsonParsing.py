import json
import os 
import requests
data = '{"name":"amit","age":22}'
result = json.loads(data)#converts into a python dictonary
print(result["name"])

student = {
    "name":"amit",
    "branch":"ce",
    "skills":["ai","ml","backend"]
}

json_data = json.dumps(student,indent=4)#converts to a json string
print(json_data)
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,"data.json")
with open(file_path,"w+") as file:
    json.dump(student,file,indent=4)
    file.seek(0)
    data = json.load(file)
    print(data)    

api_data = requests.get("https://dummyjson.com/test")
api_response = api_data.json()
print(api_response)