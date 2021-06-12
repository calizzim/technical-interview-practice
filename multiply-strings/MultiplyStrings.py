class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        toAdd = [1] * len(num1)
        for index in range(len(toAdd)): toAdd[index] *= 10 ** index
        for i in range(len(num1)-1,-1,-1):
            nextAdd = 0
            remainder = 0
            for j in range(len(num2)-1,-1,-1):
                val = int(num1[i]) * int(num2[j]) + remainder
                nextAdd += (val % 10) * 10 ** (len(num2) - j - 1)
                remainder = val // 10
            nextAdd += remainder * 10 ** len(num2)
            toAdd[len(num1) - i - 1] *= nextAdd
        return str(sum(toAdd))

s = Solution()
print(s.multiply('123', '1234'))



