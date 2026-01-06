class Solution(object):
    def isPalindrome(self, s):
        # 1. Clean the string: keep only alphanumeric characters and lowercase them
        m = "".join(char.lower() for char in s if char.isalnum())
        
        # 2. Initialize pointers
        left = 0
        right = len(m) - 1
        
        # 3. Loop until pointers meet
        while left < right:
            if m[left] == m[right]:
                left += 1
                right -= 1
            else:
                return False 
        
        return True