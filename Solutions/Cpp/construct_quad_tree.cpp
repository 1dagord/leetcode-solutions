/*
    [MEDIUM]
    427. Construct Quad Tree

    Concepts:
    - matrix
    - divide and conquer

    Stats:
        Runtime | 34 ms     [Beats 5.43%]
        Memory  | 30.50 MB  [Beats 5.65%]
*/

/*
// Definition for a QuadTree node.
class Node {
public:
bool val;
bool isLeaf;
Node* topLeft;
Node* topRight;
Node* bottomLeft;
Node* bottomRight;

Node() {
    val = false;
    isLeaf = false;
    topLeft = NULL;
    topRight = NULL;
    bottomLeft = NULL;
    bottomRight = NULL;
}

Node(bool _val, bool _isLeaf) {
    val = _val;
    isLeaf = _isLeaf;
    topLeft = NULL;
    topRight = NULL;
    bottomLeft = NULL;
    bottomRight = NULL;
}

Node(bool _val, bool _isLeaf, Node* _topLeft, Node* _topRight, Node* _bottomLeft, Node* _bottomRight) {
    val = _val;
    isLeaf = _isLeaf;
    topLeft = _topLeft;
    topRight = _topRight;
    bottomLeft = _bottomLeft;
    bottomRight = _bottomRight;
}
};
*/

class Solution {
public:
    std::vector<std::vector<int>>& branch(
        std::vector<std::vector<int>> mat
        , bool is_top
        , bool is_left
    ) {
        uint8_t n = mat.size();
        std::vector<std::vector<int>>* kernel = new std::vector<std::vector<int>>(n/2, std::vector<int>(n/2));

        uint8_t i_start = (is_top) ? (0) : (n/2);
        uint8_t j_start = (is_left) ? (0) : (n/2);

        for (uint8_t i = 0; i < n/2; i++)
            for (uint8_t j = 0; j < n/2; j++)
                kernel->at(i).at(j) = mat[i+i_start][j+j_start];

        return *kernel;
    }
    
    Node* construct(vector<vector<int>>& grid) {
        const uint8_t n = grid.size();
        std::array<uint8_t, 2> counts = {0, 0};

        for (uint8_t i = 0; i < n; i++) {
            for (uint8_t j = 0; j < n; j++) {
                counts[grid[i][j]]++;

                if (counts[0] && counts[1]) {
                    return new Node(
                        1
                        , false
                        , construct(branch(grid, true, true))
                        , construct(branch(grid, true, false))
                        , construct(branch(grid, false, true))
                        , construct(branch(grid, false, false))
                    );
                }
            }
        }

        return new Node(grid[0][0], true);
    }
};