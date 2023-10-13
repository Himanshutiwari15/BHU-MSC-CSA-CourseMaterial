from collections import defaultdict
from queue import Queue

# Graph represented as adjacency list
adj_list = defaultdict(list)


def BFS(source):

    q = Queue()
    q.put(source)
    visited = set()

    while not q.empty():
        curr = q.get()
        print(curr, end=' ')
        visited.add(curr)

        for neighbor in adj_list[curr]:
            if neighbor not in visited:
                q.put(neighbor)
                visited.add(neighbor)


# Sample graph
if __name__ == '__main__':

    adj_list[0] = [1, 2]
    adj_list[1] = [0, 3, 4]
    adj_list[2] = [0, 4]
    adj_list[3] = [1, 4, 5]
    adj_list[4] = [1, 2, 3, 5]
    adj_list[5] = [3, 4]

    BFS(0)  # 0 1 2 3 4 5
