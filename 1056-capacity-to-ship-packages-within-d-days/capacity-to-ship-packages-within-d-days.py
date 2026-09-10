def canship(weights, days, capacity):
    #find the days needed to ship all the weights under chosen capacity
    current_weight=0
    days_needed=1
    for weight in weights:
        if current_weight+weight<=capacity:
            current_weight+=weight
        else:
            days_needed+=1
            current_weight=weight
    #Compare days_needed<=days(capacity is a valid choice)
    return days_needed<=days

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low=max(weights)
        high=sum(weights)
        while low<high:
            mid=(low+high)//2
            if canship(weights, days, mid):
                high=mid
            else:
                low=mid+1
        return low