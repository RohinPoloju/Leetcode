class Solution:
    def rotateCheck(self, str1, str2):
        n = len(str1)-1
        if str1 == str2 or (str1 == "" and str2 == ""):
            return True
        if (len(str1) != len(str2)) or (set(str1) != set(str2)):
            return False
        i = 0
        while i < len(str1):
            str1 = str1[n:] + str1[:n]
            if str1 == str2:
                return True
            i += 1
        return False

sol = Solution()
print(sol.rotateCheck("rohin","rojkn"))
