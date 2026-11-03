class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        minRes = nums[0]

        while l <= r:
            if nums[l] < nums[r]:
                minRes = min(minRes, nums[l])
                break
            
            m = (l + r) // 2
            minRes = min(minRes, nums[m])

            if nums[r] < nums[m]:
                l = m + 1
            else:
                r = m - 1
        return minRes