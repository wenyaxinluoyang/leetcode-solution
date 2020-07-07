#
# 输出最长回文子串
# @param s string字符串
# @return string字符串
#
class Solution:
    def longestPalindrome(self, s):
        ans = self.solution2(s)
        return ans

    # Manacher算法
    def solution2(self, s):
        temp = '#'
        for ch in s:
            temp = temp + ch + '#'
        length = len(temp)
        p = dict()
        max_right = 0
        center = 0
        max_len = 0
        start = 0
        for i in range(length):
            p[i] = 0
            if i < max_right:
                # 计算镜像点
                mirror = center*2 - i
                p[i] = min(max_right-i, p[mirror])
            # 进行中心扩散
            left = i - (1 + p[i])
            right = i + (1 + p[i])
            while(left>=0 and right<length and temp[left]==temp[right]):
                p[i] = p[i] + 1
                left = left - 1
                right = right + 1
            if max_right < i + p[i]:
                max_right = i + p[i]
                center = i
            if p[i] > max_len:
                max_len = p[i]
                start = (i - max_len) // 2
        return s[start: start+max_len]

    # 中心扩散法
    def solution1(self , s):
        # write code here
        length = len(s)
        max_len = 0
        start, end = 0, length
        for i in range(length):
            # 以i为中心
            j = 0
            while (i-j>=0 and i+j<length and s[i-j] == s[i+j]):
                j = j + 1
            if 2*(j-1)+1 > max_len:
                max_len = 2*(j-1) + 1
                start = i - j + 1
                end = i + j
            # 以i为左边
            j = 0
            while(i-j>=0 and i+1+j<length and s[i-j]==s[i+1+j]):
                j = j + 1
            if 2*j > max_len:
                max_len = 2*j
                start = i - j + 1
                end = i + 1 + j
        return s[start:end]


if __name__ == '__main__':
    input = 'sjflsjfafjsjfareoureoi'
    s = Solution()
    ans = s.longestPalindrome(input)
    print(ans)