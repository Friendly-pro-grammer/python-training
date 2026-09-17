def square_nums(nums):
    for i in nums:
        yield (i*i)
n=square_nums([1,2,3,4,5])
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
# print(next(n))
for num in n:
    print(num)