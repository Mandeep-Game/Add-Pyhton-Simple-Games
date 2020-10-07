### here You can Use This Code For Finding same Numbers in array
def Array_Inter(arr1,n,arr2,m):   ## HEre i am Creating Function for The Program
    for i in range(n) :
        for j in range(m) :
            if arr1[i] == arr2[j] :
                print(arr1[i], end = " ")
                break
t=int(input("Test cases: "))  ## take test cases To be run
for k in range(t):
    n=int(input("Size of Array One: ")) ## Size of array By The user
    arr1=[int(x) for x in input().split()]  ## Inputs for user seperated  by Space
    m=int(input("Size Of Array Two: "))  ## Size of Array 2
    arr2=[int(y) for y in input().split()]  ## Inputs by user space seperated
Array_Inter(arr1,n,arr2,m)
