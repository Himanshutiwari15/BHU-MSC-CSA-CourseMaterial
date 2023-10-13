import heapq


class Node:

    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

    def __eq__(self, other):
        return self.freq == other.freq


def printCodes(node, val=""):
    if(node.left):
        printCodes(node.left, val + "0")
    if(node.right):
        printCodes(node.right, val + "1")

    if(not node.left and not node.right):
        print(f"{node.char} -> {val}")


def HuffmanEncoding(data):

    freq = {}
    for c in data:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1

    pq = []
    for c in freq:
        node = Node(c, freq[c])
        heapq.heappush(pq, node)

    while len(pq) > 1:
        left = heapq.heappop(pq)
        right = heapq.heappop(pq)

        parent = Node(None, left.freq + right.freq)
        parent.left = left
        parent.right = right
        heapq.heappush(pq, parent)

    printCodes(pq[0])


data = "abcdef"
HuffmanEncoding(data)
