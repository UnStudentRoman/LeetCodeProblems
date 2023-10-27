class Solution:
    def trap(self, height) -> int:
        pointer = 1
        rain_water = 0
        while pointer < len(height) - 1:
            left_max = max(height[:pointer])
            right_max = max(height[pointer + 1:])
            rain_water_capability = min(left_max, right_max) - height[pointer]
            if rain_water_capability > 0:
                rain_water += rain_water_capability
            pointer += 1
        return rain_water



if __name__ == '__main__':
    height = [0,1,0,2,1,0,1,3,2,1,2,1]

    obj = Solution()
    print(obj.trap(height))
