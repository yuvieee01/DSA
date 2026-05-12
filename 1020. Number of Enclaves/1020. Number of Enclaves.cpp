/*
 * Problem: 1020. Number of Enclaves
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/number-of-enclaves/
 * Language: cpp
 * Date: 2026-05-12
 */

class Solution {
private:
    int directions[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};
    void dfs(int i, int j, vector<vector<int>>& grid) {
        grid[i][j] = 2;

        int row = grid.size();
        int col = grid[0].size();

        for(auto& d : directions){
            int x = i + d[0];
            int y = j + d[1];
            if (x >= 0 && x < row && y >= 0 && y < col && grid[x][y] == 1){
                dfs(x, y, grid);
            }
        }
    }
public:
    int numEnclaves(vector<vector<int>>& grid) {
        int row = grid.size();
        int col = grid[0].size();

        for (int j = 0; j < col; j++) {
            if (grid[0][j] == 1){
                dfs(0, j, grid);
            }
            if (grid[row-1][j] == 1) {
                dfs(row-1, j, grid);
            }
        }
        for (int i = 0; i < row; i++) {
            if (grid[i][0] == 1){
                dfs(i, 0, grid);
            }
            if (grid[i][col-1] == 1) {
                dfs(i, col-1, grid);
            }
        }
        int res = 0;

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < col; j++) {
                if ( grid[i][j] == 1){
                    res++;
                }
            }
        }
        return res;
    }
};
