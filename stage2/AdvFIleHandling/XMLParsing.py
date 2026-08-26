import xml.etree.ElementTree as ET
import os
xml_data = """
<student>
    <name>amit</name>
    <age>22</age>
</student>
"""
root = ET.fromstring(xml_data)
print(root.tag)
print(root.find("name").text)
print(root.find("age").text)

for student in root.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    
    print(name,age,"1")
    
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,"data.xml")

tree = ET.parse(file_path)
root1 = tree.getroot()

for student in root1.findall("student"):
    name = student.find("name").text
    age = student.find("age").text
    major = student.find("major").text
    
    print(name , age ,major)
    
    
#create xml data using python
car = ET.Element("car")
maker = ET.SubElement(car,"maker")
maker.text = "Toyota"
engine = ET.SubElement(car,"engine")
engine.text ="CVT"

car_tree = ET.ElementTree(car)
car_tree.write("car.xml")