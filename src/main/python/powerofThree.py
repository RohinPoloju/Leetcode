class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n > 0:
            if round(pow(n,0.33)-int(pow(n,0.33)),1) in [0.0,0.9]:
                print(True)
            else:
                print(False)
        else:
            print(False)

sol = Solution()
sol.isPowerOfThree(27)