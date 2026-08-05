class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set=set()
        #Approach: Sort + Two Pointer(Two Sum II Approach)
        #for i in range(len(nums)):
        #    for j in range (i+1, len(nums)):
         #       for k in range (j+1, len(nums)):
          #          t_sum=nums[i]+nums[j]+nums[k]
           #         if t_sum==0:
            #            triplet=[nums[i],nums[j],nums[k]]
             #           triplet.sort()
              #          result_set.add(tuple(triplet))
        #return list(result_set)
        nums.sort()
        #Fix one value (i and run Two Sum Approach for the remaining array)
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                triplet=(nums[i],nums[left],nums[right])
                t_sum=sum(triplet)
                if t_sum==0:
                    result_set.add(triplet)
                    left+=1
                    right-=1
                elif t_sum>0:
                    right-=1
                else:
                    left+=1
        return list(result_set)