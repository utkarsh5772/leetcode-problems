class Solution(object):
    def reverseWords(self, s):
        a=s.split()
        d=[]
        for i in range(len(a)-1,-1,-1):
            d.append(a[i])
        return " ".join(d)




        
        