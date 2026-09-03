class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        d={}
        for i in nums:
            d[i]=d.get(i, 0)+1
        for i in d.keys():
            if d[i]>1:
                return True
        else:
            return False