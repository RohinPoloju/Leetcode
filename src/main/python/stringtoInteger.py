'''
This program is to convert a string to integer

Test cases:
    Input: "4187 and words"
    Output: 4187
    
    Input :"words and 783"
    Output: 0
    
    Input:"-42" or "   -42"
    Output:-42
    
     
'''
class Solution:
    def myAtoi(self,str):
        str = str.strip()
        str = list(str)
        if (len(str)==1 and str[0] == "-") or str == []:
            return 0
        else:
            if str[0] == "-" or str[0].isdigit() or str[0] == "+":
                for i in range(1, len(str)):
                    if not str[i].isdigit():
                        str = str[:i]
                        break
            else:
                return 0
        sti = ""
        for i in str:
            sti += i
        sti = ""
        for i in str:
            sti += i
        if sti == "-" or sti == "+":
            return 0
        sti = int(sti)
        if sti in range(-2**31, 2**31-1):
            return(int(sti))
        elif sti<0:
            return (-2**31)
        else: 
            return(2**31-1)
sol = Solution()
str = ""
print(sol.myAtoi(str))