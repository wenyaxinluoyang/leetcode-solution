#include<iostream>
#include<string>
#include<string.h>

using namespace std;

const int maxn = 3000;

bool dp[maxn][maxn];

class Solution {
public:
    bool isMatch(const char *s, const char *p) {
        memset(dp, false, sizeof(dp));
        string s_str = toString(s);
        string p_str = toString(p);
        int s_len = s_str.length();
        int p_len = p_str.length();
        // // 空串只能匹配空串或*
        // if(s_len == 0) {
        //     if (p_len == 0 or p_str=="*") return true;
        //     else return false;
        // }
        dp[0][0] = true;
        // 初始化，和空的s匹配。
        for(int j = 0; j < p_len; j++) {
            if(p_str[j]=='*' and dp[0][j-1]==true) {
                dp[0][j+1] = true;
            }
        }
        for(int i = 0; i < s_len; i++) {
            for(int j = 0; j < p_len; j++) {
                if(s_str[i] == p_str[j] or p_str[j]=='.') {
                    dp[i+1][j+1] = dp[i][j];
                }
                if(p_str[j] == '*') {
                    char ch = p_str[j-1];
                    if(ch == '.' or ch == s_str[i]) {
                        //dp[i+1][j-1] 匹配0个字符。
                        //dp[i+1][j] 匹配1个
                        //dp[i][j+1] 匹配多个
                        dp[i+1][j+1] = dp[i+1][j-1] | dp[i+1][j] | dp[i][j+1];
                    } else {
                        // 匹配不上，跳过这个字符
                        dp[i+1][j+1] = dp[i+1][j-1];
                    }
                }
            }
        }
        return dp[s_len][p_len];
    }

    string toString(const char *s) {
        string new_str = "";
        while(*s != '\0') {
            new_str += *s;
            s++;
        }
        return new_str;
    }
};

//"ab",".*c"  false
int main() {
    char s[] = "";
    char p[] = "mis*is*p*.";
    Solution t;
    bool flag = t.isMatch(s, p);
    cout<<flag<<endl;
    return 0;
}