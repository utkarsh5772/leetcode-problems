class Solution(object):
    def singleNumber(self, nums):
        counts = Counter(nums)
        result = []
        non_repeated = [item for item, count in counts.items() if count == 1]
        for x in range(0,len(non_repeated)):
            index = 0
            for num in nums:
             if non_repeated[x] != num:
                index ^= num
            result.append(index)
        return result         
