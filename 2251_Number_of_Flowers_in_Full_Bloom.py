class Solution:
    def fullBloomFlowers(self, flowers, people):
        bloom_dict = {i:0 for i in people}
        for flower in flowers:
            for bloom_day in range(flower[0], flower[1] + 1):
                if bloom_day in bloom_dict:
                    bloom_dict[bloom_day] += 1
        return [bloom_dict[i] for i in people]





if __name__ == '__main__':
    flowers = [[1,6],[3,7],[9,12],[4,13]]
    people = [2, 3, 7, 11]

    obj = Solution()
    print(obj.fullBloomFlowers(flowers, people))