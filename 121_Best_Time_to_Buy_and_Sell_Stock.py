class Solution:
    def maxProfit(self, prices) -> int:
        l = 0
        r = 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[l]:
                if profit < prices[r] - prices[l]:
                    profit = prices[r] - prices[l]
                r += 1
            else:
                l = r
                r = l + 1

        return profit


if __name__ == '__main__':
    prices = [7, 1, 5, 3, 6, 4]

    obj = Solution()
    print(obj.maxProfit(prices))
