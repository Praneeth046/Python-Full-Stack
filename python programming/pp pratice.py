def is_prime(num):
    fc=0
    for i in range(1,num+1):
        if num%i==0:
            fc+=1
    if fc==2:
        print("prime")
    else:
        print("not prime")
n=int(input())
is_prime(n)