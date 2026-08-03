class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for word in strs:
            res += str(len(word))+"#"+ word
        return res

    def decode(self, s: str) -> List[str]:
        i=0
        res=[]

        while i<len(s):
            j=i
            while s[j] != "#":
                j+=1
            n = int(s[i:j])
            res += [s[j+1:j+n+1]]
            i = j+n+1
        return res
