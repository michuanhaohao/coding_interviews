'''
Count the number of prime numbers less than a non-negative number, n.
'''

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return 0
        notprimes = [1] * (n-1)
        notprimes[0:1] = [0,0] 
        notprimes[2] = 1
        for i in range(2,n):
            if notprimes[i] == 1:
                notprimes[i*i:n:i] = [0] * len(notprimes[i*i:n:i])
        return sum(notprimes)