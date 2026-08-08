class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeroCount=0
        maxLength=0
        left=0
        for right in range(len(nums)):
            if nums[right]==0:
                zeroCount+=1
                #find invalid state, until valid shrink
            while zeroCount>k:
                #shrink()
                if nums[left]==0:
                    zeroCount-=1
                left+=1
            #update maxLength
            maxLength=max(maxLength, right-left+1)
        return maxLength
            