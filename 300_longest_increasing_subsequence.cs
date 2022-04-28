public class Solution {
    public int LengthOfLIS(int[] nums) {
        int n = nums.Length;
        
        int[] dp = new int[n];
        
        int res = 0;
        
        for(int i=0; i<n; i++){
            dp[i] = 1;
            for(int j=i-1; j>=0; j--){
                if(nums[j] < nums[i]){
                    dp[i] = Math.Max(dp[i], dp[j]+1);
                }
            }
            
            res = Math.Max(res, dp[i]);
        }
        
        return res;
    }
}