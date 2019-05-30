class Solution:
    def topThree(self, nums):
        i = 0
        n = 0
        for j in range(len(nums)):
            if (n < 3):
                if nums[i] != nums[j]:
                    i = j
                    n += 1
            else:
                return nums[:i]

nums = [1,1,1,2,2,2.3,3,3,4,5]
sol = Solution()
print(sol.topThree(nums)) 