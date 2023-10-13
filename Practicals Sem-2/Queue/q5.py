from collections import deque


def printMax(arr, n, k):
    Q = deque()
    for i in range(k):
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)

    for i in range(k, n):
        print(arr[Q[0]], end=" ")
        while Q and Q[0] <= i-k:
            Q.popleft()
        while Q and arr[i] >= arr[Q[-1]]:
            Q.pop()
        Q.append(i)
    print(arr[Q[0]])


if __name__ == '__main__':
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = 5
    printMax(arr, len(arr), k)
