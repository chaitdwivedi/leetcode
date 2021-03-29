'''
Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.



Example 1:


Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]

Example 2:
    Input: board = [["a","b"],["c","d"]], words = ["abcb"]
Output: []


Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 12
board[i][j] is a lowercase English letter.
1 <= words.length <= 3 * 104
1 <= words[i].length <= 10
words[i] consists of lowercase English letters.
All the strings of words are unique.
'''


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        directions = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1),
        ]

        def is_constrained(i, j):
            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return False
            return True

        def find_word(word, index, i, j):
            visited.add((i, j))

            if index == len(word) - 1:
                return True

            index = index + 1

            for i_offset, j_offset in directions:
                new_i, new_j = i + i_offset, j + j_offset
                if is_constrained(new_i, new_j) and board[new_i][new_j] == word[index] and (new_i, new_j) not in visited:
                    return find_word(word, index, new_i, new_j)

            return False

        result = set()

        rows, columns = len(board), len(board[0])
        for word in words:
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == word[0]:
                        visited = set()
                        if find_word(word, 0, i, j):
                            result.add(word)

        return list(result)

