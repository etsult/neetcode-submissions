class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}

        for word in strs:

            keys = [0]*26
            for char in word:
                keys[ord(char)-ord("a")] +=1
            if tuple(keys) in d:
                d[tuple(keys)] += [word]
            else:
                d[tuple(keys)] = [word]
        return list(d.values())
            