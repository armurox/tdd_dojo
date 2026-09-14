# Part 1
def is_anagram(word_1: str, word_2: str) -> bool:
    return sorted(word_1) == sorted(word_2)

# Part 2
def find_anagrams(target: str, words: list[str]) -> bool:
    ans = []
    for word in words:
        if is_anagram(word, target):
            ans.append(word)
    return ans
