### here You Can Use This Program As Finding Pairs Of The Number Given by user and it will return the Three number which become as one pair
def pairsum(li,n,y):  ## I created It As A function
    pairs=0
    for i in range(n):
        for j in range(i+1,n):
            for more in range(j+1,n):
                x=li[i]+li[j]+li[more]
                if (x==y):
                    pairs=pairs+1

    return pairs
t=int(input())  ## take Test Cases By user
for k in range(t):
    n=int(input())  ## take Size Of The Array
    li=[int (x) for x in input().split()] ## take Inputs by user seperated By space within The Size of The Array
    y=int(input())  ## Number for Which Pair Need to be Find
print(pairsum(li,n,y))