class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        def char_count(word):
            count = {}
            for char in word:
                count[char] = count.get(char, 0) + 1
            return count

        required_counts = {}
        for word in words2:
            word_count = char_count(word)
            for char, count in word_count.items():
                required_counts[char] = max(required_counts.get(char, 0), count)

        result = []
        for word in words1:
            word_count = char_count(word)
            if all(word_count.get(char, 0) >= count for char, count in required_counts.items()):
                result.append(word)

        return result
        