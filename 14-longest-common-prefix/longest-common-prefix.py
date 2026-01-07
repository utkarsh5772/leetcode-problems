class Solution(object):
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""

        strs.sort()

        string_1 = strs[0]
        string_2 = strs[-1]
        index = 0

        while index < len(string_1) and index < len(string_2):
            if string_1[index] == string_2[index]:
                index += 1
            else:
                break

        return string_1[:index]
