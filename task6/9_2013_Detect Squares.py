import collections
class DetectSquares:
    def __init__(self):
        self.d = collections.Counter()
        self.x= collections.defaultdict(collections.Counter)  

    def add(self, point):
        x, y = point
        self.d[x, y] += 1
        self.x[x][y] += 1

    def count(self, point):
        x, y = point
        ans = 0
        for y2 in self.x[x]:
            if y == y2: continue
            ans += self.d[x, y2] * self.d[x + y2 - y, y] * self.d[x + y2 - y, y2]
            ans += self.d[x, y2] * self.d[x + y - y2, y] * self.d[x + y - y2, y2]
        return ans