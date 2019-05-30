class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        d = {"3": "Fizz", "5": "Buzz"}
        a = []
        if n==1:
            return ["1"]
        for i in range(1,n+1):
            str1 = ""
            for k in d.keys():
                if i % int(k) == 0:
                    str1 += d[k]
            
            print(i, str1)
            if str1 == "":
                a.append(str(i))
            else:
                a.append(str1)
        print(a)

sol = Solution()
sol.fizzBuzz(15)       