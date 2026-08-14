class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix=list(itertools.accumulate(nums,initial=0))
        n=len(nums)
        for i in range(n):
            leftSum=prefix[i]
            rightSum=prefix[n]-prefix[i+1]
            if leftSum==rightSum:
               return i 
        else:
            return -1
    