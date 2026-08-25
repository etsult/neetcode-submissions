class Solution:
    def isValid(self, s: str) -> bool:
        close_to_open = {
            ")":"(",
            "]":"[",
            "}":"{"
        }
        print(close_to_open.values())
        stack = []
        for par in s:
            if par in close_to_open.values():
                stack.append(par)
            else:
                if not stack:
                    return False
                else:
                    if stack[-1] == close_to_open[par]:
                        stack.pop()
                    else:
                        return False
        return len(stack)==0