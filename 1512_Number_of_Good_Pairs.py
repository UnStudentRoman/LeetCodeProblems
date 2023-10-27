from random import randrange
import time

class Solution:
    def numIdenticalPairs(self, nums) -> int:
        return sum({i: sum(range(nums.count(i))) for i in nums}.values())




def test_fast():
    nums = [randrange(0, 20) for i in range(20000)]

    t0 = time.time()

    obj = Solution()
    obj.numIdenticalPairs(nums)

    delta = time.time() - t0
    print(delta)
    assert delta