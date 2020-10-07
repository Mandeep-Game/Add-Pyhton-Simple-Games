### This Program will basically teach You How to Find Unique number In Array Input By User
### You Can Make Fucntion Out OF This. By Just Defining The Function For It.
t=int(input())  ## This Will Take Test Case To be Run:
for k in range(t):
    n=int(input())  ## This Will Take Size Of the Array For User, Incase t=0, then It won't Run:
    li=[int(x) for x in input().split()] ## This Will Take Number Seperated By Space
    length=len(li)
    flag=0
    for i in range(0,length):
        for j in range(0,length):
            if(i==j):
                continue
            elif (li[i]==li[j]):
                flag=1
                break
        if (flag==0):
            print(li[i])
        flag=0