class Solution:
        def searchInsertPosition(self,nums,target):
            if nums == []:
                return 0
            if len(nums)==1:
                if nums[0] <= target:
                    return 1
                else:
                    return 0
            else:
                for i in range(0,len(nums)):
                    if nums[i] >=  target:
                        return i
                return len(nums)
                    
                


nums = [1,2,3,6,7]
target = 8
sol = Solution()
print(sol.searchInsertPosition(nums, target))