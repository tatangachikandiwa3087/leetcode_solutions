class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        #nums.append(0) //adds a 0 to the end
        count =0
        count1=0
        for i in nums:
            if i==1:
                count+=1
            else:
                count1=max(count,count1)
                count=0
        return max(count,count1)

