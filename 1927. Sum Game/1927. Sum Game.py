#
# Problem: 1927. Sum Game
# Difficulty: Medium
# Link: https://leetcode.com/problems/sum-game/?envType=daily-question&envId=2026-08-23
# Language: python3
# Date: 2026-08-23


# Optimal:
'''
This is the standard $O(N)$ time and $O(1)$ space solution. It relies on the mathematical proof that Bob can always balance the board perfectly using a mirroring strategy (adding 9 for every pair of ?), provided he gets the last turn.
'''
class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        half = n // 2
        
        s1, s2 = 0, 0
        q1, q2 = 0, 0
        
        # Iterate through the first half manually for strict O(N) performance
        for i in range(half):
            if num[i] == '?':
                q1 += 1
            else:
                s1 += int(num[i])
                
        # Iterate through the second half
        for i in range(half, n):
            if num[i] == '?':
                q2 += 1
            else:
                s2 += int(num[i])
        
        # Rule 1: If total '?' is odd, Alice gets the final turn.
        # She can simply pick a digit that ruins Bob's balance.
        if (q1 + q2) % 2 != 0:
            return True
        
        # Rule 2: Bob gets the final turn.
        # Every pair of '?' on a side guarantees an increase of exactly 9 to that side.
        # Bob wins ONLY if the initial sum difference perfectly offsets this future growth.
        # The right side will grow by (q2 - q1) / 2 pairs, multiplied by 9.
        return float(s1 - s2) != 9.0 * (q2 - q1) / 2.0
'''
# Pythonic Way:
This approach executes the exact same $O(N)$ math logic as the optimal solution but leverages Python's highly optimized built-in string slicing, count(), and generator comprehensions. It is much shorter, more readable, and often runs faster in practice due to underlying C implementations.

class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left, right = num[:half], num[half:]
        
        # Use built-in generator expressions to sum digits cleanly
        s1 = sum(int(c) for c in left if c != '?')
        s2 = sum(int(c) for c in right if c != '?')
        
        # Use built-in C-optimized count() for the question marks
        q1, q2 = left.count('?'), right.count('?')
        
        # Combine the odd-count rule and the mathematical offset into one return statement.
        # Multiplying by 4.5 is identical to multiplying by 9 and dividing by 2.
        return (q1 + q2) % 2 != 0 or (s1 - s2) != (q2 - q1) * 4.5
'''
'''
# Brute Force:
This approach uses Game Theory (Minimax) with memoization. Alice plays to maximize her chance of winning (returning True), while Bob plays to minimize it (returning False).Note: This is purely for educational purposes to understand the game tree. It will result in a Time Limit Exceeded (TLE) on LeetCode because the time complexity is $O(10^Q)$, where $Q$ is the number of question marks.

from functools import lru_cache

class Solution:
    def sumGame(self, num: str) -> bool:
        n = len(num)
        left, right = num[:n//2], num[n//2:]
        
        # Calculate initial sums and '?' counts
        s1 = sum(int(c) for c in left if c != '?')
        s2 = sum(int(c) for c in right if c != '?')
        q1 = left.count('?')
        q2 = right.count('?')
        
        @lru_cache(None)
        def play(q1: int, q2: int, diff: int, is_alice_turn: bool) -> bool:
            # Base Case: The board is full. 
            # Alice wins if sums are unequal (diff != 0).
            if q1 == 0 and q2 == 0:
                return diff != 0
            
            if is_alice_turn:
                # Alice wants to return True. She needs AT LEAST ONE winning move.
                # She tries digits 0-9 on the left side (if '?' available)
                if q1 > 0:
                    for d in range(10):
                        if play(q1 - 1, q2, diff + d, False): 
                            return True
                # She tries digits 0-9 on the right side (if '?' available)
                if q2 > 0:
                    for d in range(10):
                        if play(q1, q2 - 1, diff - d, False): 
                            return True
                # If no move leads to a win, Bob wins.
                return False 
            
            else:
                # Bob wants to return False. He needs AT LEAST ONE winning move.
                # He tries digits 0-9 on the left side
                if q1 > 0:
                    for d in range(10):
                        if not play(q1 - 1, q2, diff + d, True): 
                            return False
                # He tries digits 0-9 on the right side
                if q2 > 0:
                    for d in range(10):
                        if not play(q1, q2 - 1, diff - d, True): 
                            return False
                # If no move forces a tie, Alice wins.
                return True 
                
        # Initial call: pass the difference between left and right sums
        return play(q1, q2, s1 - s2, True)
'''
