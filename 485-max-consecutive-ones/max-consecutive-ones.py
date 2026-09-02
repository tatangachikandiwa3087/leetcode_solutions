class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left = 0
        maximum = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                left=right+1
            else:
                maximum=max(maximum, right-left+1)

        return maximum

