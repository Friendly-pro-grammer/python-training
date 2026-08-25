from collections import Counter,defaultdict,deque
numbers = [1,2,3,3,2,5,3,3,2,4,7,5,2,4]
count = Counter(numbers)
count1 = Counter("hello world what is the time here")
count1.update("l")
print(count)
print(count1.most_common)
print(count1.most_common(2))


freq = defaultdict(int)
str = "hello world"
for x in str:
    freq[x]+=1
print(freq)

#use to group values
students = [
    ("CE","amit",1),
    ("ce","john",2),
    ("it","pankaj",3),
    ("it","aish",4)
]
groups = defaultdict(list)
for department,name,rol in students:
    print(department,name)
    groups[department].append(name)
print(groups)


#deque-double ended queue

d = deque([1,2,3])

d.append("s")

print(d)

d.appendleft(0)

d.pop()
d.popleft()

d.appendleft((1,2,3))
print(d)
d.extend((4,5,6))
print(d)
