/*
 * Problem: 994. Rotting Oranges
 * Difficulty: Medium
 * Link: https://leetcode.com/problems/rotting-oranges/
 * Language: cpp
 * Date: 2026-05-12
 */

class Solution {
public:
    int orangesRotting(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>>dirs = {{-1,0},{1,0},{0,-1},{0,1}};

        int res = 0;

        queue<pair<int,int>>q;
        int freshCnt = 0;

        for ( int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 2) {
                    q.push({i,j});
                }
                if (grid[i][j] == 1) {
                    freshCnt++;
                }
            }
        }
        if (freshCnt == 0) {
            return 0;
        }

        while (!q.empty()) {
            int size = q.size();
            bool flag = false;
            for( int i = 0; i < size; i++) {
                auto curr = q.front();
                q.pop();
                int x = curr.first;
                int y = curr.second;
                
                for ( auto d : dirs) {
                    int r = x + d[0];
                    int c = y + d[1];

                    if (r>=0 && r<m && c>=0 && c<n && grid[r][c]==1) {
                        q.push({r,c});
                        grid[r][c] = 2;
                        flag = true;
                    }
                }
            }
            if (flag) {
                res++;
            }
        }
        for (int i = 0; i<m; i++) {
            for (int j = 0; j<n; j++) {
                if (grid[i][j] == 1) {
                    return -1;
                }
            }
        }
        return res;
    }
};
