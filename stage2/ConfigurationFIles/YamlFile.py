import yaml
import os
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir,"data.yaml")
with open(file_path,"r") as file:
    config = yaml.safe_load(file)
    
print(config)