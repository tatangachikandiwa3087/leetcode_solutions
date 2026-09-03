class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest=nums[0]+nums[1]+nums[2]
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                csum=nums[i]+nums[left]+nums[right]
                if abs(csum-target)<abs(closest-target):
                    closest=csum
                if csum<target:
                    left+=1
                elif csum>target:
                    right-=1
                else:
                    return target
        return closest