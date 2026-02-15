from functools import reduce

# 1 Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]

# l = [[1, 2], [3, 4], [5, 6]]
# k = list(map(lambda x: x + [5], l))
# print(k)

## 2 Given a dictionary: d = {"apple": 100, "banana": 40, "cherry": 150} . Use
#filter() to keep only the keys whose values are greater than 50

# d={"apple":100,"banana":40,"cherry":150}
# print(d.keys())
# print(d.values())
# print(d.items())
# f=dict(filter(lambda x:x[1]>50,d.items()))
# print(f)


## 3 Use functools.reduce() with a lambda to find the largest number from a given
#list Dynamically.

# k=list(map(int,input().split()))
# m=-10**6
# for i in k:
#     if m<i:
#         m=i
# from functools import reduce
# print(reduce(lambda x,y: x if x>y else y, k))
# print(m)

## 6  Use filter() to remove all vowels from a string and print the final string

# v = "AEIOUaeiou"
# st = list(filter(lambda x: x not in v,input()))
# print(st)


## 7  Use reduce() to concatenate a list of characters into a single string.
#Example input: ['P', 'y', 't', 'h', 'o', 'n']

# l=['x','y','z','a','b','c']
# st=reduce(lambda x,y: x+y,l)
# print(st)

## 8  Given a list of integers, use map() with id() to print the memory address
# of each element.
# Example: [10, 350, 10, 350, 20] — explain why some addresses repeat.

# l = [10, 350, 10, 350, 20]
# k = list(map(lambda x: id(x), l))
# print(k)