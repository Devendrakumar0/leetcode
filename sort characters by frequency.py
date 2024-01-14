def frequency_sort(s):
    char_freq = {}
    for char in s:
        char_freq[char] = char_freq.get(char, 0) + 1
    sorted_chars = sorted(char_freq.keys(), key=lambda x: char_freq[x], reverse=True)
    result = ""
    for char in sorted_chars:
        result += char * char_freq[char]
    return result

