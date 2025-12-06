class Solution(object):
    def moveZeroes(self, nums):
        left = 0
        for rigth in range(0,len(nums)):
            if(nums[rigth] != 0):
                 nums[rigth] , nums[left] = nums[left] , nums[rigth]
                 left +=1
        return nums         


       
        