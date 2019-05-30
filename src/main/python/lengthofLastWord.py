class Solution:
        def lengthOfLastWord(self,s):
            p = list(s)
            cnt = 0
            for i in p:
                if i == " ":
                    cnt +=1
            if len(p) == cnt:
                return 0
            else:
                return len(s.rsplit()[-1])
                
sol = Solution()
s = "   "
print(sol.lengthOfLastWord(s))