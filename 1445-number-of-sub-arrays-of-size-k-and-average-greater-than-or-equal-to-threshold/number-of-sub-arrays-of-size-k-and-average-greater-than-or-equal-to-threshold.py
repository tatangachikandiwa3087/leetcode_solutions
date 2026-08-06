class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        first_window=arr[:k]
        current_sum=sum(first_window)
        count=0
        if current_sum/k>=threshold:
            count+=1
        for i in range(k, len(arr)):
            #Adding new element to current_sum
            #subracting old element(left most element in window)
            current_sum+=arr[i]-arr[i-k]
            if current_sum/k>=threshold:
                count+=1
        return count