class Solution {
public:
    double findMaxAverage(vector<int>& nums, int k) {
        double MaxSum=0;
double a=0;
for(int i=0;i<k;i++){
a+=nums[i];
}
MaxSum=a;
for(int i=k;i<nums.size();i++){
a=a+nums[i]-nums[i-k];
MaxSum=max(MaxSum,a);
}
return MaxSum/k;
    }
};