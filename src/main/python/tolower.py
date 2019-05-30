class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        lower_str = ""
        for i in str:
            if ord(i) in range(65,91):
                lower_str += chr(ord(i)+32)
            else:
                lower_str += i
        print(lower_str) 
        
sol = Solution()
sol.toLowerCase("HellO")
