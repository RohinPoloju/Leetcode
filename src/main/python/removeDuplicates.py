class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        for j in range(len(nums)-1):
            print(i,j, nums)
            if nums[j] != nums[j+1]:
                i += 1
                nums[i],nums[j] = nums[j],nums[i]
                                
        print(nums)
        print(len(set(nums)))

sol = Solution()
sol.removeDuplicates([0,0,1,1,1,2,2,3,3,4])