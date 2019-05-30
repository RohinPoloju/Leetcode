class Solution:
    def addDigits(self, num):
        while(num >= 10):
            a = []
            sum = 0
            while(num >= 10):
                a.append(num%10)
                num = num//10
            a.append(num)
            for i in range(0, len(a)):
                sum += a[i]
            num = sum
        print(num)

sol = Solution()
num = 38
sol.addDigits(num)
