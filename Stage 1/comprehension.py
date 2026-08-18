#examples
numbers = [x**0.5 for x in range(1,101)]
nums =[x  for x in range(1,101) if (x**0.5).is_integer()]
print(nums)
num2 = [x*2 for x in range(11)]
print(num2)
names = ["amit","yadav","here"]
name_upper=[name.upper() for name in names]
print(name_upper)


#-------dict-comprehension
students = {
    "Amit": 85,
    "Rahul": 72,
    "John": 91
}
names1 = [name for name in students]
marks = [mark for mark in students.values()]

squares = {x:x**2 for x in range(1,11)}
print(squares)

marks = {
    "Amit": 85,
    "Rahul": 72,
    "John": 91,
    "Sara": 65
}
marks_80_plus = {name:marks for name,marks in marks.items() if marks>80}
print(marks_80_plus)