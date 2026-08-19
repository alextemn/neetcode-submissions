class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        out = []
        anagram_dict = {}
        
        for word in strs:
            letter_mapping = [0] * 26
            for letter in word:
                letter_mapping[ord(letter) - ord('a')] += 1
            letter_mapping = tuple(letter_mapping)
            if letter_mapping not in anagram_dict:
                anagram_dict[letter_mapping] = []
            anagram_dict[letter_mapping].append(word)
        
        for obj in anagram_dict:
            out.append(anagram_dict[obj])
        
        return out