#
# 考虑，空白， 空格，非数字字符，正负号，溢出等问题。
# @param str string字符串
# @return int整型
#
class Solution:
    def atoi(self , str ):
        min_int = -(1<<31)
        max_int = (1<<31)-1
        str = str.strip()
        if str == '': return 0
        sign = 1
        if str[0] == '-':
            sign = -1
            str = str[1: len(str)]
        elif str[0] == '+':
            str = str[1: len(str)]
        length, end = len(str), len(str)
        for i in range(length):
            if str[i]>='0' and str[i]<='9': continue
            else:
                end = i
                break
        str = str[0: end]
        if str == '': return 0
        else:
            ans = sign*int(str)
            if ans < min_int:
                ans = min_int
            if ans > max_int:
                ans = max_int
            return ans

if __name__ == '__main__':
    input = '2147483646'
    s = Solution()
    ans = s.atoi(input)
    print(ans)