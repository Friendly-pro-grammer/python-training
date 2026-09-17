#file context manager
from contextlib import contextmanager
import os 
class Open_File():
    def __init__(self,filename,mode):
        self.filename = filename
        self.mode = mode
        
    def __enter__(self):
        self.file = open(self.filename,self.mode)
        return self.file
    def __exit__(self,a,b,c):
        self.file.close()
script_dir = os.path.dirname(os.path.abspath(__file__))

file_path = os.path.join(script_dir,"example.txt")
print(file_path)
with Open_File(file_path,'w') as file:
    file.write("used a context manager here")

#using a function contex manager
@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
    finally: 
        f.close()
with open_file(file_path,'w') as file:
    file.write("used a fn context manager here")
