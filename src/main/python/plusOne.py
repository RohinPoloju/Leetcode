class Solution:
        def plusOne(self, digits):
            s = ""
            for i in digits:
                s += str(i)
            s = str(int(s)+1)
            p = []
            for i in list(s):
                p.append(int(i))
            return p
sol = Solution()
digits = [9,9]
print(sol.plusOne(digits))   