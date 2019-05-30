class Solution:
    def isValid(self,s):
        index1 = s.index('(')
        index2 = s.index(')')
        index3 = s.index('{')
        index4 = s.index('}')
        index5 = s.index('[')
        index6 = s.index(']')
        
sol = Solution()
s="(())"
sol.isValid(s) 