# [Ebay]
# design a stack structure by array.
class stack(object):
	def __init__(self, length):
		self.array = [0]*length
		self.pos = 0


	def push(self, num):
		self.array[pos] = num
		self.pos += 1
		if pos == len(self.array):
			self.array = self.array + [0]*self.pos

	def pop(self):
		res = self.array[self.pos]
		self.pos -= 1
		if self.pos <= len(self.array)/4:
			self.array = self.array[0:self.pos] + [0]*(len(self.array)/2-self.pos)
		return res
		