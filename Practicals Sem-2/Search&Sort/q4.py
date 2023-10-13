# from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distSq(p1, p2):
    return (p1.x - p2.x)*(p1.x - p2.x) + (p1.y - p2.y)*(p1.y - p2.y)


def bruteForce(P, n):
    min_val = float('inf')
    for i in range(n):
        for j in range(i + 1, n):
            if distSq(P[i], P[j]) < min_val:
                min_val = distSq(P[i], P[j])
    return min_val


if __name__ == '__main__':
    P = [Point(2, 3), Point(12, 30), Point(40, 50),
         Point(5, 1), Point(12, 10), Point(3, 4)]
    n = len(P)
    print("The smallest distance is", bruteForce(P, n))
