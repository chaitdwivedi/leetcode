'''
You are given an array of unique strings wordlist where wordlist[i] is 6 letters long, and one word in this list is chosen as secret.

You may call Master.guess(word) to guess a word. The guessed word should have type string and must be from the original list with 6 lowercase letters.

This function returns an integer type, representing the number of exact matches (value and position) of your guess to the secret word. Also, if your guess is not in the given wordlist, it will return -1 instead.

For each test case, you have exactly 10 guesses to guess the word. At the end of any number of calls, if you have made 10 or fewer calls to Master.guess and at least one of these guesses was secret, then you pass the test case.



Example 1:

Input: secret = "acckzz", wordlist = ["acckzz","ccbazz","eiowzz","abcczz"], numguesses = 10
Output: You guessed the secret word correctly.
Explanation:
master.guess("aaaaaa") returns -1, because "aaaaaa" is not in wordlist.
master.guess("acckzz") returns 6, because "acckzz" is secret and has all 6 matches.
master.guess("ccbazz") returns 3, because "ccbazz" has 3 matches.
master.guess("eiowzz") returns 2, because "eiowzz" has 2 matches.
master.guess("abcczz") returns 4, because "abcczz" has 4 matches.
We made 5 calls to master.guess and one of them was the secret, so we pass the test case.
Example 2:

Input: secret = "hamada", wordlist = ["hamada","khaled"], numguesses = 10
Output: You guessed the secret word correctly.


Constraints:

1 <= wordlist.length <= 100
wordlist[i].length == 6
wordlist[i] consist of lowercase English letters.
All the strings of wordlist are unique.
secret exists in wordlist.
numguesses == 10
'''

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def get_matches(string1, string2):
            '''Return number of matches'''
            match = 0
            for char1, char2 in zip(string1, string2):
                if char1 == char2:
                    match += 1
            return match

        def update_wordlist(current_word, api_matches):
            '''Update wordlist based on last api match result

            If 0 matches are returned by api - that means
            no char in current_word is in last place

            so any word in wordlist that has any char + pos
            matching current_word should be removed

            If 0 < matches < len(word) is returned by api
            all words that have less than this api_matches
            should be removed from wordlist
            '''
            remove_items = set()

            for word in wordlist:
                matches = get_matches(word, current_word)
                if api_matches == 0 and matches != 0:
                    remove_items.add(word)

                if api_matches != 0 and matches < api_matches:
                    remove_items.add(word)

            for item in remove_items:
                wordlist.remove(item)


        wordlist = set(wordlist)

        # perform at max of 1o iterations
        for i in range(10):
            if not wordlist:
                break

            word = wordlist.pop()
            matches = master.guess(word)

            if matches == len(word):
                return True

            update_wordlist(word, matches)

        return False
