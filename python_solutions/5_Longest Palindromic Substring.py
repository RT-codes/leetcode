# 5. Longest Palindromic Substring
# Solved
# Medium
# Topics
# Companies
# Hint

# Given a string s, return the longest
# palindromic
# substring
# in s.

 

# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.

# Example 2:

# Input: s = "cbbd"
# Output: "bb"

 

# Constraints:

#     1 <= s.length <= 1000
#     s consist of only digits and English letters.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        max_palindrome = ""
        for i in range(len(s)):
            # Odd length palindromes
            odd_palindrome = expandAroundCenter(i, i)
            if len(odd_palindrome) > len(max_palindrome):
                max_palindrome = odd_palindrome

            # Even length palindromes
            even_palindrome = expandAroundCenter(i, i + 1)
            if len(even_palindrome) > len(max_palindrome):
                max_palindrome = even_palindrome

        return max_palindrome