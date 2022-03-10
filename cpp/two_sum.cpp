#include <iostream>
#include <vector>
#include <map>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution {
public:
    /**
     * https://leetcode-cn.com/problems/two-sum/
     **/
    std::vector<int> twoSum(std::vector<int>& nums, int target) {
        std::map<int,int> hash;          //提供一对一的hash
        std::vector<int> result(2, -1);  //用来承载结果，初始化一个大小为2，值为-1的容器
        for(std::vector<int>::size_type i=0; i<nums.size(); i++) {
            if(hash.count(target-nums[i])>0) {
                result[0] = hash[target-nums[i]];
                result[1] = i;
                break;
            }
            hash[nums[i]] = i;           //反过来放入map中，用来获取结果下标
        }
        return result;
    };

    /**
     * https://leetcode-cn.com/problems/add-two-numbers/
     **/
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode *head = nullptr, *tail = nullptr;
        int carry = 0, sum, n1, n2;
        while (l1 || l2) {
            n1 = l1 ? l1->val: 0;
            n2 = l2 ? l2->val: 0;
            sum = n1 + n2 + carry;
            if (!head) {
                head = tail = new ListNode(sum % 10);
            } else {
                tail->next = new ListNode(sum % 10);
                tail = tail->next;
            }
            carry = sum / 10;
            if (l1) {
                l1 = l1->next;
            }
            if (l2) {
                l2 = l2->next;
            }
        }
        if (carry > 0) {
            tail->next = new ListNode(carry);
            tail = tail->next;
        }
        return head;
    }

};

void testTwoSum() {
    std::vector<int> nums{3, 2, 4};
    Solution solver;
    auto res = solver.twoSum(nums, 6);
    std::cout << "[" << res[0] << ", " << res[1] << "]" << std::endl;
}

int main() {
    testTwoSum();
    return 0;
}