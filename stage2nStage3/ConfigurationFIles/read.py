import configparser
import os
config =  configparser.ConfigParser()
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"config.ini")
config.read(file_path)

print(config["database"]["host"])
print(config["api"]["api_key"])
print(config.sections())
config.set('database','ssl','true')

with open(file_path,"w+") as file:
    config.write(file)