class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        char_to_word = {}
        word_to_char = {}
        
        for pat_char, word in zip(pattern, words):
            if pat_char in char_to_word:
                if char_to_word[pat_char] != word:
                    return False
            else:
                if word in word_to_char:
                    return False
                char_to_word[pat_char] = word
                word_to_char[word] = pat_char
        
        return True
        
        