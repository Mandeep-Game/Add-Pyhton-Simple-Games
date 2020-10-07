## Here You can Use This Program To Find Duplicate Entries IN Array Given By The User:
t=int(input())  ## Take Test Case To Be Run
for k in range(t):
    n=int(input())  ### Take Size Of Array
    li=[int(x) for x in input().split()] ## take Inputs Seperated By Spaces
    for i in range(0,n):
        for j in range(i+1,n):
            if (li[i]==li[j]):
                print(li[i])
#<!---------You Can Use this As Fucntion By Def it and taking Inputs Outside The Defined Fucntions--->