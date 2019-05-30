class Solution:
        def merge(self,nums1,m,nums2,n):
            nums1 = nums1 + [0]*n 
            for i in range(m,m+n):
                nums1[i] = nums2[i-(m+n)+n]
            print(sorted(nums1))

sol = Solution()
nums1 = [1,2,3]
nums2 = [2,3,4]
m = 3
n = 3
sol.merge(nums1, m, nums2, n)