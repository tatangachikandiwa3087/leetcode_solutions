class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        maxcount=1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                count+=1
            else:
                maxcount=max(count, maxcount)
                count=1
        return max(count, maxcount)