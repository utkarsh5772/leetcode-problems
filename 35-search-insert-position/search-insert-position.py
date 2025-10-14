class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        left,right,mid = 0, len(nums)-1,0

        while left <=right:
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid+1
            elif target < nums[mid]:
                right = mid-1
        
        if target < nums[mid]:
            return mid
        else :
            return mid+1