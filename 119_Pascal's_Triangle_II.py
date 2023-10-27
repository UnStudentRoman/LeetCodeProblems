class Solution:
    def getRow(self, rowIndex):
        i = 0
        result = [1]
        while i < rowIndex:
            i += 1
            inter = [0 for i in range(i + 1)]
            inter[0] = inter[-1] = 1
            inter[1] = inter[-2] = i
            for val in range(len(inter) - 3):
                inter[val+2] = result[val+2] + result[val+1]
            result = inter
        return result



if __name__ == '__main__':
    row = 8
    obj = Solution()
    print(obj.getRow(row))