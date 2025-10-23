class Solution(object):
    def singleNonDuplicate(self, nums):
        for x in range(0, len(nums) - 1, 2): 
            if nums[x] != nums[x + 1]:
                return nums[x]
        return nums[-1]  
