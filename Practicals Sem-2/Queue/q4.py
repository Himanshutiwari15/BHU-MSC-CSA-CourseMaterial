import heapq

class PriorityQueue:
    def __init__(self):
        self.heap = []

    def push(self, item, priority):
        heapq.heappush(self.heap, (-priority, item))  # Negate the priority for a max-heap

    def pop(self):
        return heapq.heappop(self.heap)[1]

    def top(self):
        return self.heap[0][1]

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.push('A', 1)
    pq.push('B', 3)
    pq.push('C', 2)

    print(pq.top()) # B (highest priority 3)

    pq.pop()

    print(pq.top()) # C (next highest priority 2)
