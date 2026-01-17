class Solution(object):
    def numIdenticalPairs(self, nums):
        count = 0
        for x in range(0,len(nums)):
            for y in range(x+1,len(nums)):
                if nums[x] == nums[y]:
                    count += 1
        return count                
        
        