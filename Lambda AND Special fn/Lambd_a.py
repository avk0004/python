"""
    USED LAMBDA , FILTER, REDUCE AND FILTER WITH BASIC KNOWNLEDGE
"""

from functools import reduce

nums = [1, 2, 3, 4, 5]
m = list(map(lambda x : x*2,nums))
print(m)

names = ["python", "java", "c++"]
x = list(map(lambda x:x.capitalize(),names))
print(x)

nums1 = [10, 15, 20, 25, 30]
p = list(filter(lambda x:x%2 ==0, nums1))
print(p)
words = ["apple", "banana", "kiwi"]
x = list(map(lambda x:len(x),words))
print(x)
marks = [45, 78, 32, 90, 66]
m = list(filter(lambda x:x>50,marks))
print(m)
nums = [5, 10, 15, 20]
m = reduce(lambda x,y:x+y,nums)
print(m)
nums = [3, 6, 9, 12]
m = list(map( lambda x:x[0]*x[1] , enumerate(nums)))
print(m)

nums = [1, 2, 3, 4, 5, 6]
l = list(filter(lambda x : x%2 ==0 ,nums))
m = reduce(lambda x,y:x*y,l)
print(m)

words = ["data", "science", "ai", "machine"]
l = reduce(lambda x,y: y+x ,map(lambda x: len(x),words),0)
print(l)