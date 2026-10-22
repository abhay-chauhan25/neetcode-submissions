class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        remaining = 0
        for num in nums:
            remaining = remaining ^ num
        return remaining