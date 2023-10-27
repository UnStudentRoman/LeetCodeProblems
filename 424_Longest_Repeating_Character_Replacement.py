class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        r = 0
        count_dict = {}
        while r < len(s):
            if s[r] not in count_dict.keys():
                count_dict[s[r]] = 1
            else:
                count_dict[s[r]] += 1
            if r - l - max(count_dict.values()) <= k:
                r += 1
            else:
                count_dict[s[l]] -= 1
                l += 1
                r += 1
        return r - l




        # while r < len(s):
        #     if s[r] not in count_dict.keys():
        #         count_dict[s[r]] = 1
        #     else:
        #         count_dict[s[r]] += 1
        #     if (r - l) - max(count_dict.values()) >= k:
        #         r += 1
        #     else:
        #         l += 1
        #         if s[l] not in count_dict.keys():
        #             count_dict[s[l]] = 1
        #         else:
        #             count_dict[s[l]] -= 1
        # return r - l


if __name__ == '__main__':
    s = "AABABBA"
    k = 1

    obj = Solution()
    print(obj.characterReplacement(s, k))