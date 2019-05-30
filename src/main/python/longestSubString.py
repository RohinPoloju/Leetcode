from _bsddb import DB_FCNTL_LOCKING
class Solution:
    def lengthOfLongestSubstring(self,s):
        if s == "":
            return 0
        arr = []
        cnt = 1
        length = 1
        for i in s:
            if arr == []:
                arr.append(i)
            else:
                if i in arr:
                    index = arr.index(i)
                    arr = arr[index+1:]
                    arr.append(i)
                    cnt = len(arr)
                else:
                    arr.append(i)
                    cnt += 1
                    length += 1
                    #if length < cnt:
                    #    length = cnt 
        if length < cnt:
            length = cnt 
        print(length,cnt)
sol = Solution()
s = "abc231231abc"
sol.lengthOfLongestSubstring(s)