# BFS

def bfs(visited, graph, node):
    visited.append(node)
    queue.append(node)

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)



visited = []
queue = []
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': [],
    'F': []
}
bfs(visited, graph, 'A')
print()

# DFS


def dfs(visted, graph, node):
    if node not in visted:
        print(node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def dfs(visited, graph, node):
    if node not in visited:
        print(node, end = " ")
        visited.add(node)
        for ngh in graph[node]:
            dfs(visited,graph,ngh)

visited = set()
dfs(visited, graph, "A")
print()

# fractionalKnapsack


def fractionalKnapsack(w, arr):
    arr.sort(key=lambda x: x[0]/x[1], reverse=True)
    finalvalue = 0

    for item in arr:
        if item[1] <= w:
            w -= item[1]
            finalvalue += item[0]
        else:
            finalvalue += item[0] * (w/item[1])
            break

    return finalvalue

def fk(w,arr):
    arr.sort(key=lambda x: x[0]/x[1], reverse = True)
    final = 0

    for item in arr:
        if item[1]<= w:
            w -= item[1]
            final += item[0]
        else:
            final += item[0] * (w/item[1])
            break
    return final



W = 50
arr = [[60, 10], [100, 20], [120, 30]]

print("Maximum value we can obtain = ", fractionalKnapsack(W, arr))

# Reverse using Stack


def revstack(str):

    if len(str) == 0 or str == None:
        return ""
    s = []
    rev = ''
    for ch in str:
        s.append(ch)

    while len(s) != 0:
        rev += s.pop()

    return rev


print('Reverse of string "Hello" is ', revstack("Hello"))

# Postfix Expression evaluation


def posexpeva(exp):
    if exp == None:
        return
    stack = []
    for ch in exp:
        if ch.isdigit():
            stack.append(ch)

        else:
            op2 = stack.pop()
            op1 = stack.pop()

            if ch == '+':
                stack.append(op2 + op1)
            
            elif ch == '-':
                stack.append(op2 - op1)
            
            elif ch =='*':
                stack.append(op2 * op1)
            
            elif ch =='/':
                stack.append(op2 / op1)
        
        return stack.pop()

# tower of hanoi

def toh(n,from_bar,to_bar,aux_bar):
    if n==1:
        print (from_bar,"->",to_bar)
        return
    else:
        toh(n-1,from_bar,aux_bar,to_bar)
        print ("Move disk ",str(n)," from bar ",from_bar ," to bar ",to_bar )
        toh(n-1,aux_bar,to_bar,from_bar)



    
def mergeSort(arr):
    if len(arr)>1:
        mid=len(arr)//2
        leftArr= arr[:mid]
        rightArr=arr[mid:]
        #sort the first half
        mergeSort(leftArr)
        mergeSort(rightArr)

        i = j =k = 0

        while i < len(leftArr) and j < len(rightArr):
            if ( leftArr[i] < rightArr[j]):
                arr[k] = leftArr[i]
                i += 1
            else:
                arr[k] = rightArr[j]
                j +=1
            k +=1
        
        while i < len(leftArr):
            arr[k] = leftArr[i]
            i += 1
            k += 1

        while j < len(rightArr):
            arr[k] = rightArr[j]
            j += 1
            k += 1




            
