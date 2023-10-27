class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        i = 0
        while i < len(s):
            if s[i] == "#":
                s = s[:i-1] + s[i+1:]
                i -= 1
            else:
                i += 1
        return s


if __name__ == '__main__':
    s = "y#fo##f"
    t = "y#f#o##f"

    obj = Solution()
    print(obj.backspaceCompare(s,t))