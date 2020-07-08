# Z字形变换

#
#
# @param s string字符串
# @param nRows int整型
# @return string字符串
#
class Solution:
    def convert(self , s , nRows):
        if s=="" or nRows==1: return s
        pos = dict()
        i, index, length = 0, 1, len(s)
        pos[0] = s[0]
        while index < length:
            # 先往下走
            k = 0
            while k < nRows-1 and index < length:
                i = i + 1
                pos[i] = pos.get(i, "") + s[index]
                index = index + 1
                k = k + 1
            # 斜着往上走
            k = 0
            while k < nRows-1 and index < length:
                i = i - 1
                pos[i] = pos.get(i, "") + s[index]
                index = index + 1
                k = k + 1
        ans = ""
        for key, value in pos.items():
            ans += value
        return ans


if __name__ == '__main__':
    s = Solution()
    # input = "A"
    # numRows = 2
    input = "LEETCODEISHIRING"
    numRows = 4
    # numRows = 3
    ans = s.convert(input, numRows)
    print(ans)

