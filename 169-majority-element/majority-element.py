class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i in d.keys():
                d[i]+=1
            else:
                d[i]=1
        n=len(nums)
        for i in nums:
            if d[i]>n/2:
                return i
        