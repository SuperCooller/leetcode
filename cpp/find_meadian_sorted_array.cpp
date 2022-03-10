#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    /**
     * https://leetcode-cn.com/problems/median-of-two-sorted-arrays/
     **/
    double findMedianSortedArrays_1(std::vector<int>& nums1, std::vector<int>& nums2) {
        auto n1 = nums1.size();
        auto n2 = nums2.size();
        std::vector<int> merge_vec;
        merge_vec.reserve(n1+n2);
        std::vector<int>::size_type i1 = 0, i2 = 0, i = 0;
        while(i1 < n1 && i2 < n2) {
            if (nums1[i1] < nums2[i2]) {
                merge_vec[i++] = nums1[i1++];
            } else {
                merge_vec[i++] = nums2[i2++];
            }
        }
        while (i1 < n1) {
            merge_vec[i++] = nums1[i1++];
        }
        while (i2 < n2) {
            merge_vec[i++] = nums2[i2++];
        }
        if ((n1 + n2) % 2 == 1) {
            return static_cast<double>(merge_vec[(n1 + n2 - 1) / 2]);
        }
        auto middle = (n1 + n2) / 2;
        return static_cast<double>(merge_vec[middle - 1] + merge_vec[middle]) / 2;
    }

    using v_size_t = std::vector<int>::size_type;
    int find_kth(std::vector<int>& A, v_size_t start_A, v_size_t end_A, 
                    std::vector<int>& B, v_size_t start_B, v_size_t end_B, 
                    v_size_t k) {
        auto size_A = end_A - start_A + 1;
        auto size_B = end_B - start_B + 1;
        std::cout << "k " << k << " size_A " << size_A << " size_B " << size_B << std::endl;
        if (size_A > size_B) {
            return find_kth(B, start_B, end_B, A, start_A, end_A, k);
        }
        if (size_A == 0) {
            return B[start_B + k - 1];
        }
        if (k == 1) {
            return std::min(A[start_A], B[start_B]);
        }
        auto middle = k / 2;
        auto ia = std::min(size_A, middle);
        auto ib = middle - ia; 
        
        auto mid_A = A[start_A + ia - 1];
        auto mid_B = B[start_B + ib - 1];
        std::cout << "k " << k << " middle " << middle << " size_A " << size_A << " ia " << ia 
                                                       << " size_B " << size_B << " ib " << ib 
                                                       << " mid_A " << mid_A << " mid_B " << mid_B << std::endl;

        if (mid_A < mid_B) {
            return find_kth(A, start_A + ia, end_A, B, start_B, end_B, k - ia);
        } else if (mid_A > mid_B) {
            return find_kth(A, start_A, end_A, B, start_B + ib, end_B, k - ib);
        } else {
            return mid_A;
        }
    }

    double findMedianSortedArrays_2(std::vector<int>& nums1, std::vector<int>& nums2) {
        auto m = nums1.size();
        auto n = nums2.size();
        auto total = m + n;
        if (total & 0x1) {
            return find_kth(nums1, 0, m - 1, nums2, 0, n -1, total / 2 + 1);
        }
        return (find_kth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2) + find_kth(nums1, 0, m - 1, nums2, 0, n - 1, total / 2 + 1)) / 2.0;
    }
};

void testFindMedianSortedArrays_1() {
    std::vector<int> nums1{1, 3};
    std::vector<int> nums2{2};
    Solution solver;
    auto res = solver.findMedianSortedArrays_1(nums1, nums2);
    std::cout << res << std::endl;
}

void testFindMedianSortedArrays_2() {
    std::vector<int> nums1{1, 3};
    std::vector<int> nums2{2};
    Solution solver;
    auto res = solver.findMedianSortedArrays_2(nums1, nums2);
    std::cout << res << std::endl;
} 

int main() {
    testFindMedianSortedArrays_1();
    testFindMedianSortedArrays_2();
    return 0;
}