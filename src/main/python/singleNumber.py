class Solution():
    def singleNumber(self,nums):
        nums = sorted(nums)
        print(nums, len(nums))
        i = 0
        while(i < len(nums)):
            print(i)
            if i+1 > len(nums)-1:
                return nums[i]
            if nums[i] == nums[i+1]:
                i+=2
            else:
                return nums[i]
        
    
sol = Solution()
nums = []
print(sol.singleNumber(nums))