#include <iostream>
#include <string>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * https://leetcode-cn.com/problems/longest-palindromic-substring/
     **/
    std::string longestPalindrome_1(std::string s) {
        auto s_size = s.size();
        std::string::size_type begin = 0;
        std::string::size_type length = 1;
        std::vector<std::vector<int>> dp(s_size, std::vector<int>(s_size));
        for (std::string::size_type i = 0; i < s_size; ++i) {
            dp[i][i] = 1;
        }
        for (std::string::size_type l = 2; l <= s_size; l++) {
            for (std::string::size_type i = 0; i < s_size; ++i) {
                auto j = l + i - 1;
                if (j > s_size - 1) {
                    break;
                }
                if (s[i] != s[j]) {
                    dp[i][j] = 0;
                } else if (l < 4) {
                    dp[i][j] = 1;
                } else {
                    dp[i][j] = dp[i + 1][j - 1];
                }
                if (dp[i][j] && l > length) {
                    begin = i;
                    length = l;
                }
            }
        }
        return s.substr(begin, length);
    }

    std::pair<int, int> expandAroundCenter(const std::string& s, int left, int right) {
        while (left >= 0 && right < s.size() && s[left] == s[right]) {
            --left;
            ++right;
        }
        return {left + 1, right - 1};
    }

    std::string longestPalindrome(std::string s) {
        int start = 0, end = 0;
        for (int i = 0; i < s.size(); ++i) {
            auto [left1, right1] = expandAroundCenter(s, i, i);
            auto [left2, right2] = expandAroundCenter(s, i, i + 1);
            if (right1 - left1 > end - start) {
                start = left1;
                end = right1;
            }
            if (right2 - left2 > end - start) {
                start = left2;
                end = right2;
            }
        }
        return s.substr(start, end - start + 1);
    }
};

void testLongestPalindrome() {
    std::string s{"bb"};
    Solution solver;
    auto res = solver.longestPalindrome(s);
    std::cout << "source s->" << s << " res->" << res << std::endl;
}

int main() {
    testLongestPalindrome();
    return 0;
}