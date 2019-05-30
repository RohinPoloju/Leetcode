class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mini = min(nums)
        maxi = max(nums)
        if maxi == 1 and mini == 0:
            print(2)
        elif len(nums) == 1 and nums[0] != 1:
            print(nums[0]+1)
        else:
            sums = sum(list(range(min(nums),max(nums)+1)))
            print(sums-sum(nums))

sol = Solution()
sol.missingNumber([1,2])