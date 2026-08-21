class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}

        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        freq_list = [ None ]*(len(nums)+1)
        for num, freq in count.items():
            if freq_list[freq] != None:
               freq_list[freq].append(num)
            else:
                freq_list[freq] = [num]
        res = []
        for i in range(len(freq_list)-1,0,-1):
            temp = freq_list[i]
            while temp:
                temp_num = temp.pop()
                res.append(temp_num)
                if len(res)==k:
                    return res