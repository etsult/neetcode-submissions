class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)==1:
            return nums[0]

        res = [0] * len(nums)
        res[-1] = nums[-1]
        res[-2] = max(nums[-2],nums[-1])
        for i in range(len(nums)-3,-1,-1):
            res[i] = max(nums[i] + res[i+2],res[i+1])
        print(res)
        return max(res[0],res[1])