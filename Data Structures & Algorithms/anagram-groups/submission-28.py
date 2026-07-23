class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        d = dict()

        for word in strs:
            keys = [0]*26
            for char in word:
                key_number= ord(char)-ord('a')
                print(key_number)
                keys[key_number] = 1 + keys[key_number]
            if d.get(tuple(keys)):
                lst = d.get(tuple(keys))
                lst.append(word)
                d[tuple(keys)] = lst
            else:
                d[tuple(keys)] = [word]
        return list(d.values())
