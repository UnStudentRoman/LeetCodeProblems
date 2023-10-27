import string

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = 0
        r = len(s1)
        s1 = sorted(s1)
        sorted_window = sorted(s2[l:r])
        while l < len(s2) - len(s1) + 1:
            if sorted_window == s1:
                return True
            else:
                l += 1
                r += 1
                sorted_window = sorted(s2[l:r])
        return False


if __name__ == '__main__':
    s1 = 'adc'
    s2 = 'dcda'

    obj = Solution()
    print(obj.checkInclusion(s1, s2))