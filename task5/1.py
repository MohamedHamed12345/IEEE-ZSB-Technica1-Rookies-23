import sys
class MaxHeap:
	def __init__(self, maxsize):
		self.maxsize = maxsize
		self.size = 0
		self.Heap = [0] * (self.maxsize + 1)
		self.Heap[0] = sys.maxsize
	def parent(self, pos):return pos // 2
	def insert(self, element):
		if self.size >= self.maxsize:return
		self.size += 1
		self.Heap[self.size] = element
		current = self.size
		while (self.Heap[current] >
			self.Heap[self.parent(current)]):
			self.swap(current, self.parent(current))
			current = self.parent(current)
	def swap(self, fpos, spos):
		self.Heap[fpos], self.Heap[spos] = (self.Heap[spos],self.Heap[fpos])		
	def Print(self):
		while self.Heap[-1]==0:self.Heap.pop()
		print(*self.Heap[1:])

if __name__ == "__main__":	
	l=list(map(int, input().split()))
	m=MaxHeap(max(l))
	for i in l:m.insert(i)
	m.Print()
