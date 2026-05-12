/*
 * Problem: 1254. Number of Closed Islands
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/number-of-closed-islands/description/
 * Language: cpp
 * Date: 2026-05-12
 */

#include <vector>
using namespace std;
class Solution {
private:
    int directions[4][2] = {{-1, 0}, {1, 0}, {0, -1}, {0, 1}};

    void dfs(int i, int j, vector<vector<int>>& grid) {
        grid[i][j] = 1;

        int row = grid.size();
        int col = grid[0].size();

        for (auto& d : directions) {
            int x = i + d[0];
            int y = j + d[1];

            if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 0) {
                dfs(x, y, grid);
            }
        }
    }
public:
    int closedIsland(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();

        for (int j = 0; j < col; j++) {
            if (grid[0][j] == 0) dfs(0, j, grid);
            if (grid[row - 1][j] == 0) dfs(row - 1, j, grid);
        }

        for (int i = 0; i < row; i++) {
            if (grid[i][0] == 0) dfs(i, 0, grid);
            if (grid[i][col - 1] == 0) dfs(i, col - 1, grid);
        }

        int res = 0;
        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if (grid[i][j] == 0) {
                    dfs(i, j, grid);
                    res++;
                }
            }
        }
        return res;
    }
};
