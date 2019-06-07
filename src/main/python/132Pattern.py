class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        for i in range(len(nums)-2):
            print(i, nums[i], nums[i+1], nums[i+2])
            if nums[i] < nums[i + 2] < nums[i + 1]:
                return True
        return False

sol = Solution()
nums = [3, 5, 0, 3, 4]
print(sol.find132pattern(nums))
