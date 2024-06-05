class Solution:
    def spread(self, dictionary):
        char_list = []
        for letter in dictionary:
            char_list += [letter]*dictionary[letter]
        return char_list
    def compare(self, dict1, dict2):
        new_dict = {}
        print(dict1, dict2)
        for letter in dict1:
            if letter in dict2:
                new_dict[letter] = min(dict1[letter], dict2[letter])
        return new_dict
    def commonChars(self, words: List[str]) -> List[str]:
        char_dictionary = Counter(words[0])
        for word in words:
            new_dictionary = {}
            for letter in word:
                if letter not in new_dictionary:
                    new_dictionary[letter] = 0
                new_dictionary[letter] += 1
            char_dictionary = self.compare(new_dictionary, char_dictionary) 
        char_list = self.spread(char_dictionary)
        return char_list 
    