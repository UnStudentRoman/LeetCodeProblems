
class Solution:
    def minCostClimbingStairs(self, cost) -> int:

        # Decide start
        # if cost[0] > cost[1]:
        #     i = 1
        # else:
        #     i = 0
        #
        # result += cost[i]

        i = 0
        result_0 = cost[i]

        while i < len(cost) - 2:
            if cost[i + 1] < cost[i + 2]:
                i += 1
            else:
                i += 2
            result_0 += cost[i]

        i = 1
        result_1 = cost[i]

        while i < len(cost) - 2:
            if cost[i + 1] < cost[i + 2]:
                i += 1
            else:
                i += 2
            result_1 += cost[i]

        return min(result_1,result_0)



if __name__ == '__main__':
    cost = [0,1,2,2]

    obj = Solution()
    print(obj.minCostClimbingStairs(cost))