class Solution():
    def strStr(self,haystack, neddle):
        h_list = list(haystack)
        n_list = list(neddle)
        if n_list == []:
            return 0
        for i in range(0, len(h_list)):
            if h_list[i] == n_list[0]:
                cnt = 1
                for j in range(1, len(n_list)):
                    if i+j > len(h_list)-1:
                        return -1
                    elif h_list[i+j] == n_list[j]:
                        cnt +=1
                    else:
                        break
                if cnt == len(n_list):
                    return i 
        return -1
        
    
sol = Solution()
haystack = "hello world"
neddle = "or"
print(sol.strStr(haystack, neddle))