class Solution:

    def threeSum(self, nums):
        nums.sort()
        answers = []
        for index, value in enumerate(nums):
            if index > 0 and value == nums[index - 1]:
                continue

            l, r = index + 1, len(nums) - 1
            while l < r:
                threeSum = value + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    answers.append([value, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return answers


if __name__ == '__main__':
    nums = [0,0,0,0,0]



    obj = Solution()

    print(obj.threeSum(nums))