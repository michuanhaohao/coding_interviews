'''
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the 6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one, with the least significant bit on the right.
Given a non-negative integer n which represents the number of LEDs that are currently on, return all possible times the watch could represent.

Example:

Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16", "0:32"]
Note:
The order of output does not matter.
The hour must not contain a leading zero, for example "01:00" is not valid, it should be "1:00".
The minute must be consist of two digits and may contain a leading zero, for example "10:2" is not valid, it should be "10:02".
'''

class Solution(object):
    def __init__(self):
        self.reslist = []
        self.state = [0] * 10 # 10个LED的状态
    
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        self.dfs(num, 0)
        return self.reslist
    
    
    def dfs(self, num, index):
        if num == 0:
            temp = self.list2Str(self.state)
            if temp != None and temp not in self.reslist:
                self.reslist.append(temp) # 找到一个可行解
            return
            
        if index > 9:
            return # 无可行解
        
        for i in range(index, 10):
            self.state[i] = 1
            self.dfs(num-1, i+1)
            self.state[i] = 0
            self.dfs(num, i+1) 
    
    def list2Str(self, slist):
        res = ""
        hour = sum([slist[i] * 2**i for i in range(4)])
        if hour > 11:
            return None # 不符合条件，舍去
        res += (str(hour) + ":")
        mins = sum([slist[i+4] * 2**i for i in range(6)])
        if mins > 59:
            return None
        if mins < 10:
            res += "0"
        res += str(mins)
        return res
		
	# 简单的方法
	def readBinaryWatch(self, num):
		return ['%d:%02d' % (h, m)
				for h in range(12) for m in range(60)
				if (bin(h) + bin(m)).count('1') == num] # bin() 将一个整形数字转换成二进制字符串