class Solution(object):
    def triangleNumber(self, nums):
        nums.sort()
        count = 0
        n = len(nums)
        for k in range(n - 1,1,-1):
            left = 0
            rigth = k - 1
            while left < rigth:
                if nums[left] + nums[rigth] > nums[k]:
                    count += rigth - left
                    rigth -= 1
                else:
                    left +=1
        return count                         
        