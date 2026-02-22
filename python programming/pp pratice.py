##Given number is prime or not

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

a=int(input())
b=int(input())
c=0
if a<b:
    for i in range(a,b+1):
        if i%2==1:
            c+=1
            if c%2==1:
                print(i)
