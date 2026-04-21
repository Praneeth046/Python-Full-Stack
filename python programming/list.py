l=[10,20,30,40,50,60,70,80,90]
# print(l)

# for i in l:
#     print(l)

# print(l[-2])

# l.append(200)
# print(l)

# l.insert(0,500)
# print(l)

## merging two lists
# list1=list(map(int,input().split()))
# list2=list(map(int,input().split()))
# merge=list1 + list2
# print(merge)

## reversing the elements in list
# l=list(map(int,input().split()))
# s=0
# e=len(l)-1
# while s<e:
#     t=l[s]
#     l[s]=l[e]
#     l[e]=t
#     s+=1
#     e-=1
# print(l)

## avg of odd numbers in list
l=list(map(int,input().split()))
sum=0
c=0
for i in l:
    if i%2==1:
        sum=sum+i
        c+=1
print(sum/c)