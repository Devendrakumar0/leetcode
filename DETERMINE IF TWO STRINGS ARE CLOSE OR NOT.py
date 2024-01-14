# Problem Description:
# You are given two strings, word1 and word2. Two strings are considered "close" if you can transform one string into the other using the following operations:

# Swap any two existing characters in the string.

# Example: "abc" -> "acb"
# Transform every occurrence of one existing character into another existing character, and do the same with the other character.

# Example: "aacabb" -> "bbcbaa" (all 'a's turn into 'b's, and all 'b's turn into 'a's)
# The goal is to determine whether word1 and word2 are close or not.
from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        count1 = Counter(word1)
        count2 = Counter(word2)
        if set(count1.keys()) != set(count2.keys()):
            return False
        if sorted(count1.values()) != sorted(count2.values()):
            return False
        return True
