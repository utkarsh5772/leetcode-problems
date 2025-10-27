class Solution(object):
    def canJump(self, nums):
        maxreach = 0
        for x in range(0,len(nums)):
            if x > maxreach:
                return False
            maxreach = max(maxreach, x + nums[x])
        return True           


