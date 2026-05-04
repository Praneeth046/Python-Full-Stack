## Aadhar validation

s=input()
if len(s)==12:
    for i in range(0,len(s)):
        if not(s[i]>="0" and s[i]<="9"):
            print("Invalid")
            break
        else:
            print("valid")