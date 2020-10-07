from copy import deepcopy
from itertools import permutations

initial = [[], ['A'], ['B', 'C']]
goal = [[], [], ['A', 'B', 'C']]
length = len(initial)

def gen_children(state):
    children = []
    for i in range(length):
        state_copy = deepcopy(state)
        if state_copy[i]:
            popped = state_copy[i].pop() # popping
            for j in range(length):
                child = deepcopy(state_copy)
                child[j].append(popped)
                children.append(child)
    return children

def dfs(node):
    closed = [] #stack
    open = [node]
    visited = []

    while open:
        node = open.pop()
        closed.append(node)
        visited.append(node)

        all_permu = permutations(node)
        for permu in all_permu:
            perm = list(permu)
            if perm == goal:
                return closed

        children = gen_children(node)

        count = 0
        buffer = []
        for next in children:
            flag = False
            all_permu = permutations(next)

            for permu in all_permu:
                perm = list(permu)
                if perm in visited:
                    flag = True
                    count += 1
                    break
            else:
                buffer.append(next)
        if count == len(children) and closed:
            closed.pop()

        else:
            for next in buffer:
                all_permu = permutations(next)
                for permu in all_permu:
                    perm = list(permu)
                    if perm in open:
                        break
                else:
                    open.append(next)
    return closed

ans = dfs(initial)
print(f'ans = ', *ans)
