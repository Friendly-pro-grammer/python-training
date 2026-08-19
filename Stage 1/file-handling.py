#to open a file open(file,mode)
# with open("/file.txt", "r") as file:
#     content = file.read()

# print(content)
with open("Stage 1/file.txt", "r") as file:
    #content = file.read()
    line = file.readline()
    line2 = file.readline()
#print line by line by using readline
with open("Stage 1/file.txt","r") as file:
    lines= file.readlines()
#print line by line using readlines

print(line,line2)
print(lines)

#best way to read large files
with open("Stage 1/file.txt","r") as file:
    for line in file:
        print(line.strip())
        
#-----writing--------to----a------file-----
#use w mode
#.write creates a new file if it doesnt exists and replaces the whole content
with open("Stage 1/file.txt","w") as file:
    file.write("hello python")
#use a mode to append to the current data

with open("Stage 1/file.txt","w") as file:
    file.write("\n new appended line")