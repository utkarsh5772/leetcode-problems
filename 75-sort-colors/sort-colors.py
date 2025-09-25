class Solution(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        count2 = 0
        for n in nums:
            if n == 0:
                count0 +=1
            elif n == 1:
                count1 += 1
            elif n == 2 :
                count2 += 1

        for x in range(0,len(nums)):
            if count0 != 0 :
                nums[x] = 0
                count0 -= 1
            elif count1 != 0:
                nums[x] = 1
                count1 -= 1
            elif count2 != 0:
                nums[x] = 2
                count2 -= 1
        return nums                              