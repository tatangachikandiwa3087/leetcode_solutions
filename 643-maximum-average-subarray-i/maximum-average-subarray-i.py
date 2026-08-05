class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #slidng window (fixe length sliding window)
        max_avg=-1000000
        left=0
        right=0
        current_sum=0
        for right in range(len(nums)):
            current_sum+=nums[right]
            if right>=k-1:
                avg=current_sum/k
                max_avg=max(avg, max_avg)
                #Subtracting the values on the left because the window size k is exceeded
                current_sum-=nums[left]
                left+=1
        return max_avg