#
#
# @param x int整型
# @return bool布尔型
#
class Solution:
    def isPalindrome(self , x):
        if x < 0: return False
        temp = x
        y = 0
        while temp != 0:
            y = y*10 + temp%10
            temp = temp//10
        if y == x: return True
        else: return False

if __name__ == '__main__':
    x = 193794287
    s = Solution()
    ans = s.isPalindrome(x)
    print(ans)
