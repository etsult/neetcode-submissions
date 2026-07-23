class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_dict = {}
        freq = [ [] for i in range(len(nums)+1)]
        res = []

        for num in nums:
            count_dict[num] = 1 + count_dict.get(num,0)
        
        for num,frequencies in count_dict.items():
            freq[frequencies].append(num)
        
        for i in range(len(freq)-1,-1,-1):
            for num in freq[i]:
                res.append(num)
                if len(res)==k:
                    return res