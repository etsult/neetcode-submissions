class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [1]*len(nums)

        for i in range(len(nums)-1,-1,-1):
            for k,num in enumerate(nums[i:]):
                if nums[i]<num:
                    dp[i] = max(1 + dp[i+k],dp[i])
        return max(dp)
