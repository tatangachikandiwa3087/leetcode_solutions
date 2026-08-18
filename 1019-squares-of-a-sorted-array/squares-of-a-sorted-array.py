class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        lst=[x*x for x in nums]
        left=0
        right=len(nums)-1
        pos=right
        result=[0]*len(nums)
        while left<=right:
            if lst[left]>lst[right]:
                result[pos]=lst[left]
                left+=1
            else:
                result[pos]=lst[right]
                right-=1
            pos-=1
        return result