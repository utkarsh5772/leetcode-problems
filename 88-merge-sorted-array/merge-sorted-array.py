class Solution(object):
    def merge(self, nums1, m, nums2, n):
        k = 0
        for x in range(m,len(nums1)):
             nums1[x] = nums2[k]
             k = k + 1
        return nums1.sort()         