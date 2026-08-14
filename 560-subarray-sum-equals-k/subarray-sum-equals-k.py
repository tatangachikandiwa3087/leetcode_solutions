class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        #Prefix + Hash Map Solution
        prefix_sum=0# this is the prefix sum 
        subCount=0#how many sub arrays have we seen with sum k
        seen={0:1}#hash maps to store the prefix sums found so far
        for i in nums:
            #compute prefix sum
            prefix_sum+=i
            #required prefix su(prefix[left-1], history)
            required=prefix_sum-k
            #check if required in seen prefixes so far
            if required in seen:
                subCount+=seen[required]#add the number of time we seen that prefix
            #push the current prefix in a hash map
            seen[prefix_sum]=seen.get(prefix_sum,0)+1
        return subCount