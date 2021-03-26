'''
Given a set of words (without duplicates), find all word squares you can build from them.

A sequence of words forms a valid word square if the kth row and column read the exact same string, where 0 ≤ k < max(numRows, numColumns).

For example, the word sequence ["ball","area","lead","lady"] forms a word square because each word reads the same both horizontally and vertically.

b a l l
a r e a
l e a d
l a d y
Note:

There are at least 1 and at most 1000 words.
All words will have the exact same length.
Word length is at least 1 and at most 5.
Each word contains only lowercase English alphabet a-z.
Example 1:

Input:
["area","lead","wall","lady","ball"]

Output:
[
  [ "wall",
    "area",
    "lead",
    "lady"
  ],
  [ "ball",
    "area",
    "lead",
    "lady"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
Example 2:

Input:
["abat","baba","atan","atal"]

Output:
[
  [ "baba",
    "abat",
    "baba",
    "atan"
  ],
  [ "baba",
    "abat",
    "baba",
    "atal"
  ]
]

Explanation:
The output consists of two word squares. The order of output does not matter (just the order of words in each word square matters).
'''

class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
	'''Naive Solution that will time out'''
    
        def can_add(matrix, word):
            '''check if you can add word to matrix'''
            tmp = matrix  + [word]
                
            limit = min(len(tmp), len(tmp[0]))
            for i in range(limit):
                for j in range(limit):
                    if tmp[i][j] != tmp[j][i]:
                        return False 

            return True
    
        def build_sq(matrix, results): 
            if len(matrix) == len(words[0]):
                results.append(matrix[:])
                return 
        
            for word in [x for x in words if can(matrix, x)]:
                matrix.append(word)
                build_sq(matrix, results)
                matrix.pop() # backtracking here 
    
        results = []
        matrix = []
        
        for word in words:
            matrix = [word]
            build_sq(matrix, results)
            
        return results
                
        
class Solution:
    def wordSquares(self, words: List[str]) -> List[List[str]]:
	'''Improved Solution using pre-compiled startswith table and prefix'''
    
        def build_table():
            '''Pre-compile a startswith table using dict and set

            dict + set will allow for O(1) lookup
            '''
            for word in words:
                for i in range(1, len(word)):
                    starts_with_table[word[:i]].add(word)

    
        def build_sq(matrix, results): 
            if len(matrix) == len(words[0]):
                results.append(matrix[:])
                return 
        
            prefix = ''.join([word[len(matrix)] for word in matrix])
            for word in starts_with_table.get(prefix, []):
                matrix.append(word)
                build_sq(matrix, results)
                matrix.pop()
    
        results = []
        matrix = []
        
        starts_with_table = defaultdict(set)
        build_table()
    
        for word in words:
            matrix = [word]
            build_sq(matrix, results)
            
        return results
