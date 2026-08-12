class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum_=[]
        s=0
        for i in nums:
            s+=i
            sum_.append(s)
        return sum_