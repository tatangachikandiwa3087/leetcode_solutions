def canship(weights, days, capacity):
    current_weight=0
    days_needed=1
    for weight in weights:
        if current_weight+weight>capacity:
            days_needed+=1
            current_weight=weight
        else:
            current_weight+=weight
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