class Solution:
    def isValid(self, s: str) -> bool:
        stack = [s[0]]
        i = 1
        closing = {")": "(",'}': '{', ']': '['}
        while i < len(s):
            if s[i] in closing: 
                if not stack:
                    return False
                if closing[s[i]] != stack.pop():
                    return False
            else:
                stack.append(s[i])
            i+=1
        return not stack