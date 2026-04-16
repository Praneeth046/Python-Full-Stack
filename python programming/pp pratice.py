##Given number is prime or not
from operator import truediv


# def is_prime(num):
#     fc=0
#     for i in range(1,num+1):
#         if num%i==0:
#             fc+=1
#     if fc==2:
#         print("prime")
#     else:
#         print("not prime")
# n=int(input())
# is_prime(n)


## To print alternative odd numbers in a given range

# a=int(input())
# b=int(input())
# c=0
# if a<b:
#     for i in range(a,b+1):
#         if i%2==1:
#             c+=1
#             if c%2==1:
#                 print(i)


##To print average of alternative prime numbers

# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#         if fc==2:
#             return True
#         else:
#             return False
# a=int(input())
# b=int(input())
# c=ac=sum=0
# for i in range(a,b+1):
#     n=is_prime(i)
#     if n==True:
#         c+=1
#         if c%2==1:
#             sum=sum+i
#             ac+=1
# print(sum/ac)



##To print maximum digit from a given number

# n=int(input())
# max=0
#     r=n%10
#     n=n//10
#     if r>max:
#         max=r
# print(max)

## To print minimum digit from a given number

# n=int(input())
# min=9
# while n>0:
# while n>0:
#     r=n%10
#     n=n//10
#     if r<min:
#         min=r
# print(min)


#program to print next prime number to a given number
# def is_prime(n):
#     fc=0
#     for i in range(1,n+1):
#         if n%i==0:
#             fc+=1
#     if fc==2:
#         return True
# n=int(input())
# i=n+1
# while True:
#     if is_prime(i):
#         print(i)
#         break
#     i+=1

#print even and odd without using division operator
#@using AND

# n=int(input())
# if n&1==0:
#     print("even")
# else:
#     print("odd")
#
# #@using OR
#
# n=int(input())
# if n|1==n+1:
#     print("even")
# else:
#     print("odd")
#
# #@using XOR
#
# n=int(input())
# if n^1==n+1:
#     print("even")
# else:
#     print("odd")

# Program to print palindrome or Not

# n=int(input())
# t=n
# rev=0
# while n>0:
#     r=n%10
#     rev=rev*10+r
#     n=n//10
# if rev==t:
#     print("palindrome")
# else:
#     print("not a palindrome")



##patterns to print rectangle
# r=int(input())
# c=int(input())
# for i in range(1,r+1):
#     for j in range(1,c+1):
#         print("*",end=" ")
#     print()


##patterns to print square
# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print("*",end="  ")
#     print()

## pattern

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(i,end=" ")
#     print()

## hollow patterns rectangle

# a=int(input())
# b=int(input())
# for i in range(1,a+1):
#     for j in range(1,b+1):
#         if (i==1 or i==a) or (j==1 or j==b):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

## hallow patterns square

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         if i==1 or i==n or j==1 or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

## hallow patterns  triangle

# n=int(input())
# for i in range(1,n+1):
#     for j in range(1,n-i+1):
#         print(" ",end="")
#     for j in range(1,i+1):
#         if j==1 or i==n or i==j:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

## hallow pattern
# n=int(input())
# for i in range(1,n+1):
#     for j in range(n-i):
#         print(" ",end="")
#     for j in range(1,n+1):
#         if i==1 or j==1 or i==n or j==n:
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


n = int(input())
if n == 0:
    print("Zero")
else:
    n = abs(n)
    i = 0
    for j in range(n):
        if i == 0:
            print("1", end="")
        elif i == 1:
            print("A", end="")
        else:
            print("@", end="")

        if j != n - 1:
            print(", ", end="")

        i += 1
        if i == 3:
            i = 0