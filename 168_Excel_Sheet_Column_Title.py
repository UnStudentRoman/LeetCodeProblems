class Solution:
    def convertToTitle(self, columnNumber):
        col_vals = "ABCDEFGHIJKLMNOPQRSTUVXYZ"
        stack = []
        while columnNumber > 26:
            stack.append(26)
            parte_intreaga = columnNumber // 26
            rest = columnNumber % 26
            columnNumber = parte_intreaga + rest
        stack.append(columnNumber)
        print(stack)
        return stack



if __name__ == '__main__':
    columnNumber = 11111
    obj = Solution()
    print(obj.convertToTitle(columnNumber))