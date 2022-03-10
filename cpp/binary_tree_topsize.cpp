#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <stdio.h>

using namespace std;

class Node {
public:
    int value;
    Node *left;
    Node *right;


    Node() : value(0), left(nullptr), right(nullptr) {}
    Node(int data) : value(data) {}
};

///////////////////////////////////////////////////////////////
// 判断node是否在以root为头节点的搜索二叉树上
bool isBSTNode(Node *h, Node *n, int value) {
    if (nullptr == h) {
        return false; 
    }
    if (h == n) {
        // 找到了
        return true;
    }
    return isBSTNode(h->value > value ? h->left : h->right, n, value);
}

// 搜索以root为头节点的最大拓扑结构
int maxTopo(Node *h, Node *n) {
    if (h != nullptr && n != nullptr && isBSTNode(h, n, n->value)) {
        // 以root为头节点的满足要求，继续从左右子树开始搜索
        return maxTopo(h, n->left) + maxTopo(h, n->right) + 1;
    }
    return 0;
}

int bstTopoSizeRec(Node *head) {
    if (nullptr == head) {
        return 0;
    }
    int max = maxTopo(head, head);
    max = std::max(bstTopoSizeRec(head->left), max);
    max = std::max(bstTopoSizeRec(head->right), max);
    return max;
}
///////////////////////////////////////////////////////////////

class Record {
public:
    int l;
    int r;

    Record() : l(0), r(0) {}
    Record(int left, int right) : l(left), r(right) {}
};

int modifyMap(Node *n, int v, std::map<Node *, Record> &map, bool is_left) {
    if (nullptr == n || 0 == map.count(n)) {
        return 0;
    }
    Record r = map[n];
    if ((is_left && n->value > v) || ((!is_left) && n->value < v)) {
        // 不符合条件，去掉整个子树的记录数
        auto it = map.find(n);
        map.erase(it);
        return r.l + r.r + 1;
    } else {
        // 符合条件，计算另一侧子树路径上的扣减值
        int minus = modifyMap(is_left ? n->right : n->left, v, map, is_left);
        if (is_left) {
            r.r = r.r - minus;
        } else {
            r.l = r.l - minus;
        }
        // 修改记录，并返回扣减值
        map[n] = r;
        return minus;
    }
    return 0;
}

int posOrder(Node *h, std::map<Node *, Record> &map) {
    if (nullptr == h) {
        return 0;
    }
    int ls = posOrder(h->left, map);
    int rs = posOrder(h->right, map);
    modifyMap(h->left, h->value, map, true);
    modifyMap(h->right, h->value, map, false);

    int lbst = 0, rbst = 0;
    auto l_it = map.find(h->left);
    if (l_it != map.end()) {
        lbst = l_it->second.l + l_it->second.r + 1;
    }
    auto r_it = map.find(h->right);
    if (r_it != map.end()) {
        rbst = r_it->second.l + r_it->second.r + 1;
    }

    map[h] = Record(lbst, rbst);
    return std::max(lbst + rbst + 1, std::max(ls, rs));
}

int bstTopoSize(Node *head) {
    std::map<Node *, Record> map;
    return posOrder(head, map);
}

#define LOCAL 1

int main() {
#ifdef LOCAL
    freopen("./in.txt", "r", stdin);
#endif
 
    int n, root;
    int rt, l, r;
    std::cin >> n >> root;
    //std::cout << n << root << std::endl;
    vector<Node> tree(n + 1);
    for (int i = 0; i < n; i++) {
        std::cin >> rt >> l >> r;
        tree[rt].value = rt;
        if (l) tree[rt].left = &tree[l];
        if (r) tree[rt].right = &tree[r];
    }
    int ans_rec = bstTopoSizeRec(&tree[root]);
    std::cout << "Rec " << ans_rec << std::endl;
    int ans = bstTopoSize(&tree[root]);
    std::cout << "Res " << ans << std::endl;
    return 0;
}