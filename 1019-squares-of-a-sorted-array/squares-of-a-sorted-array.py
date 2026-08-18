class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=[x*x for x in nums]
        lst.sort()
        return lst