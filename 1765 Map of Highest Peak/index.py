    LeetCode Logo

Problem List
22
Premium
Debugging...
Debugging...
Description
Testcase
Testcase
Test Result
Test Result
Accepted
Accepted
Editorial
Editorial
Solutions
Solutions
Submissions
Submissions
Code
Code
Map of Highest Peak
Map of Highest Peak
Code Sample
1765. Map of Highest Peak
Solved
Medium
Topics
Companies
Hint

You are given an integer matrix isWater of size m x n that represents a map of land and water cells.

    If isWater[i][j] == 0, cell (i, j) is a land cell.
    If isWater[i][j] == 1, cell (i, j) is a water cell.

You must assign each cell a height in a way that follows these rules:

    The height of each cell must be non-negative.
    If the cell is a water cell, its height must be 0.
    Any two adjacent cells must have an absolute height difference of at most 1. A cell is adjacent to another cell if the former is directly north, east, south, or west of the latter (i.e., their sides are touching).

Find an assignment of heights such that the maximum height in the matrix is maximized.

Return an integer matrix height of size m x n where height[i][j] is cell (i, j)'s height. If there are multiple solutions, return any of them.

 

Example 1:

Input: isWater = [[0,1],[0,0]]
Output: [[1,0],[2,1]]
Explanation: The image shows the assigned heights of each cell.
The blue cell is the water cell, and the green cells are the land cells.

Example 2:

Input: isWater = [[0,0,1],[1,0,0],[0,0,0]]
Output: [[1,1,0],[0,1,1],[1,2,2]]
Explanation: A height of 2 is the maximum possible height of any assignment.
Any height assignment that has a maximum height of 2 while still meeting the rules will also be accepted.

 

Constraints:

    m == isWater.length
    n == isWater[i].length
    1 <= m, n <= 1000
    isWater[i][j] is 0 or 1.
    There is at least one water cell.

 

Note: This question is the same as 542: https://leetcode.com/problems/01-matrix/
Seen this question in a real interview before?
1/5
Yes
No
Accepted
35.6K
Submissions
54.8K
Acceptance Rate
65.1%
Topics
Array
Breadth-First Search
Matrix
Companies
Hint 1
Set each water cell to be 0. The height of each cell is limited by its closest water cell.
Hint 2
Perform a multi-source BFS with all the water cells as sources.
Discussion (37)
💡 Discussion Rules

1. Please don't post any solutions in this discussion.

2. The problem discussion is for asking questions about the problem or for sharing tips - anything except for solutions.

3. If you'd like to share your solution for feedback and ideas, please head to the solutions tab and post it there.
No comments yet.
Copyright ©️ 2025 LeetCode All rights reserved
2882 Online
Runtime: 666ms
python

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        row = len(isWater)
        col = len(isWater[0])

        height = [[-1]*col for _ in range(row)]
        q = deque()

        for i in range(row):
            for j in range(col):
                if isWater[i][j] == 1:
                    q.append((i, j))
                    height[i][j] = 0

        d = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while q:
            x, y = q.popleft()
            for dx, dy in d:
                nx = x + dx
                ny = y + dy
                if nx < 0 or nx == row or ny < 0 or ny == col:
                    continue
                if height[nx][ny] != -1:
                    continue
                
                height[nx][ny] = height[x][y] + 1
                q.append((nx, ny))

        return height

