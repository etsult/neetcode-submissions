class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        #left
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *=nums[i]
        
        print(res)
        print(prefix)
        
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            print(i,postfix,res[i])
            res[i] = res[i]*postfix
            postfix *=nums[i]

        return res