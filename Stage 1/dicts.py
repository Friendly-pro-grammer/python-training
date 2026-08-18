#example of dict
#mutable mapping to associate key and values
#keys must be unique,values can be duplicated
#keys must be hashable
student = {
    "name":"amit",
    "age":22,
    "course":"CSE"
}
#access 
print(student["name"],student["course"])#this throws keyerror when no value 
print(student.get("age"))#this throws none
#add a new key
student["city"]="Modasa"
#update a key
student["age"]=23
#add multiple key value pairs using update
student.update({
    "batch":2027,
    "cgpa":9.28
})
#update with keyword arguments
student.update(age=22)
#remove a key
student.pop("age")

#to remove everything use .clear(method)
#student.clear()
#to get keys
print(student.keys())
#to get values 
print(student.values())
#iterating throught the dictionlary
print("------")
for keys in student.keys():
    print(keys)
for values in student.values():
    print(values)
#both key and value
for key,value in student.items():
    print(key,value)
#dictionaries preserve the inserion order
#nested dictionaries
s1 = {
    "name":"john",
    "age":33,
    "course":"EC"
}
#list of dictionaries
s2 = [
    {
        "name":"amit"
    },{
        "name":"john"
    }
]
