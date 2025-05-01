class Solution(object):
    def removeElement(self, nums, val):
        n  = len(nums)
        index = 0
        for x in range(n):
            if nums[x] != val:
                nums[index] = nums[x]
                index += 1
        return index  
        