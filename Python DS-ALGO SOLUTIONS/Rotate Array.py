### Simply Use to rotate array but main Feature is that:
# 1. it will rotate by user Index, You Will Not find It on internet
def rotatearray(arr, n, d) :
    k=0
    temp=[]
    while k!=d:
        temp.append(arr[k])
        k+=1
    k=0
    while k!=d:
        arr.remove(temp[k])
        k+=1
    k=d
    for i in temp:
        arr.append(i)
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()
t=int(input())  ## Take Number Of Test Cases To be Runned
while t>0:
    n=int(input())  ## Take Size of The Array
    arr=[int(x) for x in input().split()]  ## Inputs for Array by Space seperated
    d=int(input("Enter The Number(Not Index):"))
    rotatearray(arr,n,d)
    printList(arr,n)
    t-=1