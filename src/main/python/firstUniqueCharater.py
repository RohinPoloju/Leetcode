class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s =="":
            return(-1)
        if len(s) == len(set(s)):
            return(0)
        d={}
        for i in s:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        for k,v in d.items():
            if v==1:
                return(s.index(k))
        return(-1)

sol = Solution()
print(sol.firstUniqChar("rohin"))