class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}

        for i, num1 in enumerate(nums):

            num2 = target - num1

            if num2 in hashMap:

                return [hashMap[num2],i]
            else:
                hashMap[num1]=i