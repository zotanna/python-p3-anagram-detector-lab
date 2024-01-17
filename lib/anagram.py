class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, word_list):
        return [w for w in word_list if self._are_anagrams(w)]

    def _are_anagrams(self, other_word):
        return sorted(self.word) == sorted(other_word.lower())
