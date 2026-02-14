# 1 Use map() with a lambda to add 5 to every element of the following nested
#list [[1, 2], [3, 4], [5, 6]]

# l = [[1, 2], [3, 4], [5, 6]]
# k = list(map(lambda x: x + [5], l))
# print(k)

## 2

d={"apple":100,"banana":40,"cherry":150}
print(d.keys())
print(d.values())
print(d.items())
f=dict(filter(lambda x:x[1]>50,d.items()))
print(f)


## 3

# k=list(map(int,input().split()))
# m=-10**6
# for i in k:
#     if m<i:
#         m=i
# from functools import reduce
# print(reduce(lambda x,y: x if x>y else y, k))
# print(m)





