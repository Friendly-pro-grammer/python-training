name="amit"
print(name[0])
print(name[::-1])
title=""""
this is a multi line string
"""
#similar slicing
print(name[0:4])
#strings are not mutable
s1="hello"
s2="world"
s="whAt   iS CsEngIneeRing     "
s3 =s1+" "+s2
print(s3)
print(s1*5)
#length
print(len(s3))
#case conversion
print(s.lower())
print(s.upper())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.strip().capitalize())
z="##abcde##"
print(z.strip("#"))
text = "I like Machine Learning"
result = text.replace("Machine","Deep")
print(result)
print(text.find("Machine"))
#find and index are almost same just find returns -1 if not found and index throws a value eror
print(text.count("e"))
print(text.startswith("I"))
print(text.endswith("ing"))
data = "python,java,cpp"
langs = data.split(",")
print(langs)

t="034234"
t1="d234rq"
#string validation methods
print(s.isalpha())
print(t.isdigit())
print(t.isalnum())

#string formatting

age=22
message = "my name is {} and i am {} years old".format(name,age)
print(message)
#f strings best way used
msg = f"my name is {name} and i am {age} years old"
print(f"you are {'adult' if age>=18 else 'minor'}")
x=3.1415129
print(f"{x:.2f}")