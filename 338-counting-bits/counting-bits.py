class Solution(object):
    def countBits(self, n):
        result = []
        for x in range(0,n+1):
            temp = bin(x)[2:]
            countones = str(temp).count('1')
            result.append(countones)
        return result    

        
        