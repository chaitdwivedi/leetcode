'''
Given two strings S and T, return if they are equal when both are typed into empty text editors. 
# means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

Example 1:

Input: S = "ab#c", T = "ad#c"
Output: true
Explanation: Both S and T become "ac".
Example 2:

Input: S = "ab##", T = "c#d#"
Output: true
Explanation: Both S and T become "".
Example 3:

Input: S = "a##c", T = "#a#c"
Output: true
Explanation: Both S and T become "c".
Example 4:

Input: S = "a#c", T = "b"
Output: false
Explanation: S becomes "c" while T becomes "b".
Note:

1 <= S.length <= 200
1 <= T.length <= 200
S and T only contain lowercase letters and '#' characters.
Follow up:

Can you solve it in O(N) time and O(1) space?
'''
class Solution:
    def stack_backspaceCompare(self, S: str, T: str) -> bool:
        '''Stack based solution

        Time: O(N)
        Space: O(N+M)
        '''
        def get_stack(string):
            stack = []
            for char in string:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return stack

        return get_stack(S) == get_stack(T)

    def backspaceCompare(self, S: str, T: str) -> bool:
        '''Pointer solution

        Time: O(N)
        Space: O(1)
        '''
        s, t = len(S) - 1, len(T) - 1
        skip_s, skip_t = 0, 0

        while s >= 0 or t >= 0:
            # skip all backspace and affected charaters
            while (s >= 0):
                # count number of backspaces and keep moving left
                if S[s] == '#':
                    skip_s += 1   # keep incrementing skip count
                    s -= 1        # keep moving left
                elif skip_s > 0:  # encounter non # char: if skips accumulated
                    skip_s -= 1   # reduce skips
                    s -= 1        # keep moving left - skipping the characters
                else:             # found first non # char unaffected by #
                    break

            while (t >= 0):
                if T[t] == '#':
                    skip_t += 1
                    t -= 1
                elif skip_t > 0:
                    skip_t -= 1
                    t -= 1
                else:
                    break

            if s >= 0 and t >= 0 and S[s] != T[t]:  # compare character
                return False

            # if one string ends and other doesn't
            if (s >= 0 and t < 0) or (t >= 0 and s < 0):
                return False

            s -= 1
            t -= 1

        return True
