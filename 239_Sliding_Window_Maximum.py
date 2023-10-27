from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k: int):
        l = 0
        stack = []
        # window = nums[l:l + k]
        stack.append((max(nums[l:l + k]), l + k - nums[l:l + k][::-1].index(max(nums[l:l + k]))))
        while l + k < len(nums):
            if nums[l + k] > stack[-1][0]:
                stack.append((nums[l + k], l + k))
                l += 1
            elif l > stack[-1][1]:
                stack.append((max(nums[l:l + k]), l + k - nums[l:l + k][::-1].index(max(nums[l:l + k]))))
                l += 1
            else:
                stack.append(stack[-1])
                l += 1

        return stack


if __name__ == '__main__':
    nums = [2,2,3,8]
    k = 2

    obj = Solution()
    print(obj.maxSlidingWindow(nums, k))