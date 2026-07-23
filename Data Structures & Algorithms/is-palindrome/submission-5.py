class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        for char in s:
            if char.isalnum():
                res += char.lower()
        print(res)

        return res == res[::-1]