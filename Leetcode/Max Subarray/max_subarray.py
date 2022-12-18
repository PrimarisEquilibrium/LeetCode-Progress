class Solution:
    def maxSubArray(self, nums: list[int]) -> int:

        largest = nums[0]
        prev = nums[0]
        
        for i in range(1, len(nums)):
            cur = nums[i]
            if cur < cur + prev:
                cur = cur + prev
            prev = cur
            largest = max(largest, cur)
        return largest