#
# 翻转给出的整数
# @param x int整型
# @return int整型
#
class Solution:
    def reverse(self , x ):
        sign = 1
        if x < 0:
            sign = -1
            x = -x
        reverse_integer = []
        while x != 0:
            reverse_integer.append(x%10)
            x = x//10
        ans = 0
        for value in reverse_integer:
            ans = ans*10 + value
        ans = ans*sign
        return ans

if __name__ == '__main__':
    s = Solution()
    # x = 123
    # x = -10100
    x = 0
    ans = s.reverse(x)
    print(ans)