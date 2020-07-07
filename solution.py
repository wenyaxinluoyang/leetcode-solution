#
#
# @param s string字符串
# @return int整型
#

class Solution:
    def lengthOfLongestSubstring(self, s):
        # write code here
        if len(s) ==0 : return 0
        length = len(s)
        ans = 1
        for i in range(length):
            for j in range(length):
                temp = s[i:j]
                my_dict = dict()
                flag = True
                for ch in temp:
                     my_dict[ch] = my_dict.get(ch, 0) + 1
                     if my_dict[ch] > 1:
                         flag = False
                         break
                if flag:
                    if len(temp) > ans: ans = len(temp)
        return ans

class Solution:
    def lengthOfLongestSubstring(self, s):
        # write code here
        if len(s) ==0 : return 0
        ans = 0
        cur = ""
        ch_pos = dict()
        for ch in s:
            exist = False
            if ch_pos.get(ch, 0) == 1:
                exist = True
            if exist == False:
                ch_pos[ch] = 1
                cur = cur + ch
            else:
                start = 0
                length = len(cur)
                for i in range(length):
                    if cur[i] == ch:
                        start = i
                        break
                    ch_pos[cur[i]] = 0
                cur = cur[start+1: len(cur)] + ch
            if len(cur) > ans: ans = len(cur)
        return ans

if __name__ == '__main__':
    input = 'bbbb'
    s = Solution()
    ans = s.lengthOfLongestSubstring(input)
    print(ans)



class Solution:
    def lengthOfLongestSubstring(self, s):
        # write code here
        if len(s) ==0 : return 0
        length = len(s)
        ans = 1
        for i in range(length):
            for j in range(length):
                temp = s[i:j]
                my_dict = dict()
                flag = True
                for ch in temp:
                     my_dict[ch] = my_dict.get(ch, 0) + 1
                     if my_dict[ch] > 1:
                         flag = False
                         break
                if flag:
                    if len(temp) > ans: ans = len(temp)
        return ans




