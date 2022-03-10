#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    bool isMatchRecur(std::string s, std::string p) {
        return is_match_1(s.c_str(), p.c_str());
    }
    bool is_match_1(const char *s, const char *p) {
        if (*p == '\0')
            return *s == '\0';
        //std::cout << s << " " << p << std::endl;
        // 以下一个字符是否是*来划分
        if (*(p+1) != '*') {
            if (*p == *s || (*p == '.' && *s != '\0'))
                return is_match_1(s+1, p+1);
            else 
                return false;
        } else {
            while (*p == *s || (*p == '.' && *s != '\0')) {
                if (is_match_1(s, p+2)) {
                    return true;
                }
                s++;
            }
            return is_match_1(s, p+2);
        }
    }

    using s_size = std::string::size_type;
    bool is_match(std::string &s, std::string &p, s_size s_start, s_size p_start) {
        auto s_length = s.size();
        auto p_length = p.size();
        //std::cout << s_start << " " << s_length << " " << p_start << " " << p_length << " " << s.substr(s_start, s_length-s_start) << " " << p.substr(p_start, p_length-p_start) << std::endl;
        // 是否已经没有字符要匹配了
        if (p_start >= p_length) {
            return (s_start >= s_length);
        }
        if (p[p_start + 1]  != '*') {
            if (p[p_start] == s[s_start] || (p[p_start] == '.' && s_start < s_length)) {
                return is_match(s, p, s_start + 1, p_start + 1);
            } else {
                return false;
            }
        } else {
            while (p[p_start] == s[s_start] || (p[p_start] == '.' && s_start < s_length)) {
                if (is_match(s, p , s_start, p_start+2)) {
                    return true;
                }
                s_start++; 
            }
            return is_match(s, p, s_start, p_start + 2);
        }
        return false;
    }
    bool isMatch_1(std::string s, std::string p) {
        return is_match(s, p, 0, 0);
    }

    /**
     * https://leetcode-cn.com/problems/regular-expression-matching/
     **/
    bool isMatch(std::string s, std::string p) {
        int m = s.size();
        int n = p.size();

        auto matches = [&](int i, int j) {
            if (i == 0) {
                return false;
            }
            if (p[j - 1] == '.') {
                return true;
            }
            return s[i - 1] == p[j - 1];
        };

        std::vector<std::vector<int>> f(m + 1, std::vector<int>(n + 1));
        f[0][0] = true;
        for (int i = 0; i <= m; ++i) {
            for (int j = 1; j <= n; ++j) {
                if (p[j - 1] == '*') {
                    f[i][j] |= f[i][j - 2];
                    if (matches(i, j - 1)) {
                        f[i][j] |= f[i - 1][j];
                    }
                }
                else {
                    if (matches(i, j)) {
                        f[i][j] |= f[i - 1][j - 1];
                    }
                }
            }
        }
        return f[m][n];
    }
};

void testIsMatch() {
    std::string src = "aaaaaaaaaaaaab";
    std::string pattern = "a*a*a*a*a*a*a*a*a*a*c";
    std::cout << src[src.size()] << (src[src.size()] == '\0') << std::endl;
    Solution solver;
    auto res_recur = solver.isMatchRecur(src, pattern);
    auto res = solver.isMatch(src, pattern);
    std::cout << src << " " << pattern << " " << res_recur << " " << res << std::endl;
}

int main() {
    testIsMatch();
    return 0;
}