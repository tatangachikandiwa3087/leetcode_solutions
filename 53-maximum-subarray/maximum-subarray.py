class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current=0
        maxi=nums[0]
        for i in nums:
          if current<0:
            current=0
          current+=i
          maxi=max(maxi, current)
        return maxi
