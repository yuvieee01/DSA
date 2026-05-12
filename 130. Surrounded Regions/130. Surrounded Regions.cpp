/*
 * Problem: 130. Surrounded Regions
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/surrounded-regions/description/
 * Language: cpp
 * Date: 2026-05-12
 */

class Solution {
private:
    int directions[4][2] = {{-1,0}, {1,0}, {0,-1}, {0,1}};

    void dfs(int i, int j, vector<vector<char>>& board){
        board[i][j] = 'S';

        int row = board.size();
        int col = board[0].size();

        for (auto& d : directions) {
            int x = i + d[0];
            int y = j + d[1];

            if (x >= 0 && x < row && y >= 0 && y < col && board[x][y] == 'O'){
                dfs(x,y,board);
            }
        }
    }
public:
    void solve(vector<vector<char>>& board) {
        int row = board.size();
        int col = board[0].size();

        for (int j = 0; j < col; j++){
            if (board[0][j] == 'O'){
                dfs(0, j, board);
            }
            if (board[row-1][j] == 'O'){
                dfs(row-1, j, board);
            }
        }
        for (int i = 0; i < row; i++){
            if (board[i][0] == 'O'){
                dfs(i, 0, board);
            }
            if (board[i][col-1] == 'O'){
                dfs(i, col-1, board);
            }
        }

        for (int i = 0; i < row; i++){
            for (int j = 0; j < col; j++){
                if (board[i][j] == 'O'){
                    board[i][j] = 'X';
                }
                if (board[i][j] == 'S'){
                    board[i][j] = 'O';
                }
            }
        }
    }
};
