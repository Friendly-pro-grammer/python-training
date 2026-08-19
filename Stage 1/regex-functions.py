#regex library and its functions
import re
text = "i have 30 apples and 20 bananas"
res = re.findall(r"\d+",text)
vowels = re.findall(r"[aeiou]",text)
print(res,vowels)

#python functions
let = "python is easy"
result = re.match(r"python",let)#returns none if not found or else returns match object
#checks at beginning
#to search for entire string use 
res1 = re.search(r"is",let)

#meanwhile findall returns the all occureences
res2 = re.findall(r"e",text)

print(res2)
