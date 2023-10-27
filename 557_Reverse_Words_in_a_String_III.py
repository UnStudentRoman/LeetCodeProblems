class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(' ')
        s = [i[::-1] for i in s]
        return ' '.join(s)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"

    obj = Solution()
    print(obj.reverseWords(s))