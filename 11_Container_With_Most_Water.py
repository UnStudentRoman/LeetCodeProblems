class Solution:
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        result = 0
        while l < r:
            container = min(height[l], height[r])*(r-l)
            if result < container:
                result = container
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return result


if __name__ == '__main__':
    height = [2,3,4,5,18,17,6]

    obj = Solution()
    print(obj.maxArea(height))