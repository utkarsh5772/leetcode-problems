class Solution(object):
    def intersection(self, nums1, nums2):
        result = []
        for i in nums1:
            if i in nums2 and i not in result:
                result.append(i)
        return result      