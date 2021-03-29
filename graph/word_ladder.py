'''
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.



Example 1:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.
Example 2:

Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.


Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.
'''
class Solution:
    '''Time Limit Exceeded'''
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def uniquify(word):
            '''use index and char to uniquify a word'''
            uniq = set()
            for i, char in enumerate(word):
                uniq.add(f"{i}{char}")
            return uniq

        def diff_by_one(word1, word2):
            '''return True if diff only by 1 char'''
            word1, word2 = uniquify(word1), uniquify(word2)
            result = len(word1.intersection(word2)) == len(word1) - 1
            return result

        def build_graph(wordList):
            '''Map words that are differing by exactly 1 character'''
            graph = defaultdict(list)
            for index, word in enumerate(wordList):
                for inner_index, iword in enumerate(wordList):
                    if inner_index != index and diff_by_one(word, iword):
                        graph[word].append(iword)
            return graph


        def find_path(graph, beginWord, endWord):
            '''Use BFs (queue) to find shortest path between
            beginWord and endWord for the given graph 
            '''
            q = deque()
            q.append((beginWord, 0))
            visited = set()

            while q:
                current, current_path = q.popleft()
                if current == endWord:
                    return current_path + 1
                visited.add(current)
                for neighbor in graph[current]:
                    if neighbor not in visited:
                        q.append((neighbor, current_path + 1))


            return 0


        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList = [beginWord] + wordList

        wordList = set(wordList)

        graph = build_graph(wordList)

        return find_path(graph, beginWord, endWord)


######################################################################################
#
# Optimized working solution
#
# Time limit exceeds in previous solution because we are checking each word for diff
# logic - which again runs for all character per word
#
# A faster solution would be to to generate all diff by 1 using ascii codes (a-z) 
# and check if the genearted neighbor exists in input wordList 
#
# i.e. build the graph on the fly - using `get_neighbors`
#
# remaining logic stays same
#
######################################################################################


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def get_neighbors(current):
            '''Generate all possible neighbors for given word

            use ascii code to generate all possibilites 
            filter out possibilites using the input wordList
            '''
            neighbors = []
            for ascii_ in range(ord('a'), (ord('z') + 1)):
                replace = chr(ascii_)
                i = 0
                while i < len(current):
                    possible_neighbor = current[:i] + replace + current[i+1:]
                    if possible_neighbor in wordList:
                        neighbors.append(possible_neighbor)
                        wordList.remove(possible_neighbor)
                    i += 1

            return neighbors


        def find_path(beginWord, endWord):
            '''Use BFS (queue) to find shortest path between 
            beginWord and endWord

            Graph here is generated on the 'fly' using get_neighbords
            '''
            q = deque()
            q.append((beginWord, 0))
            visited = set()

            while q:
                current, current_path = q.popleft()
                if current == endWord:
                    return current_path + 1
                visited.add(current)
                for neighbor in get_neighbors(current):
                    if neighbor not in visited:
                        q.append((neighbor, current_path + 1))


            return 0


        if endWord not in wordList:
            return 0

        if beginWord not in wordList:
            wordList = [beginWord] + wordList

        wordList = set(wordList)

        return find_path(beginWord, endWord)
