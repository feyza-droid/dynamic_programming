"""
Say that you are a traveler on a 2D grid. 
You begin in the top-left corner and your goal is to travel to the bottom-right corner.
You may only move down or right.
"""

# starting from top-left corner, iterate through from left to right and then top to bottom by adding current value to both to down and right
def gridTraveler(m, n):
    row, col = m + 1, n +1
    table = [[0 for _ in range(col)] for _ in range(row)] # (m+1 x n+1) or (row x col) matrix
    table[1][1] = 1

    for r in range(row): # you can start from index 1 instead of 0 as well, since there is no way from 0,0
        for c in range(col): # you can start from index 1 instead of 0 as well, since there is no way from 0,0
            if r+1 < row: table[r+1][c] += table[r][c] # down
            if c+1 < col: table[r][c+1] += table[r][c] # right

    return table[m][n]

print(gridTraveler(1, 1)) # 1
print(gridTraveler(2, 3)) # 3
print(gridTraveler(3, 2)) # 3
print(gridTraveler(3, 3)) # 6
print(gridTraveler(18, 18)) # 2333606220

# time complexity O(m*n)