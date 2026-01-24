class Solution(object):
    def trap(self, height):
       left = 0
       rigth = len(height) - 1
       maximum_left = height[left] 
       maximum_rigth = height[rigth]
       water = 0

       while left < rigth:
            if maximum_left < maximum_rigth:
             left += 1
             maximum_left = max(maximum_left,height[left])
             water += maximum_left - height[left]
            else:
                rigth -= 1
                maximum_rigth = max(maximum_rigth,height[rigth])
                water += maximum_rigth - height[rigth]
       return water
            
             
     