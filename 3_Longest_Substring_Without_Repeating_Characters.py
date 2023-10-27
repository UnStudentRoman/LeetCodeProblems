class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        l = 0
        r = 1
        answer = 0
        sub_str = s[l]
        while r < len(s):
            if s[r] not in sub_str:
                sub_str += s[r]
                r += 1
            else:
                if answer < len(sub_str):
                    answer = len(sub_str)
                l += 1
                sub_str = s[l]
                r = l +1
        if answer < len(sub_str):
            answer = len(sub_str)
        return answer


if __name__ == '__main__':
    s = "ababababadsakjndfkashjbfgvkjlasbdjkla kjhvbajsklfbhjadbjnasljfbvjkhabfkjasnfkhsdbfhalsjfblsebfjlk;asnjfkbsdkfhasnfjlksdflasnjlkfvhbsdkjfsdlkbfgsdaaaabbb"

    obj = Solution()
    print(obj.lengthOfLongestSubstring(s))