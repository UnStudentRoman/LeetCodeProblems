class Solution:
    def minOperations(self, nums):
        inter = [0 for num in nums]
        nums = list(set(nums))
        nums.sort()
        i = 0
        j = 0
        min = nums[0]
        while i < len(nums):
            if nums[i] - min < len(inter):
                inter[j] = nums[i]
                del nums[i]
                j += 1
            else:
                i += 1
        return inter.count(0)


if __name__ == '__main__':
    vals = [41,33,29,33,35,26,47,24,18,28]

    obj = Solution()
    print(obj.minOperations(vals))