from typing import List


class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviations = {}

        for word in dictionary:
            abbr = self.getAbbreviation(word)

            if abbr not in self.abbreviations:
                self.abbreviations[abbr] = {word: word}
            else:
                self.abbreviations[abbr][word] = word

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbreviation(word)

        # 1. if word abbreviation does not match anything in the dict, return True
        # 2. if there are more than one matches for the abbreviation, return False
        # 3. If there is only one match, return True if the word is the same

        if abbr not in self.abbreviations:
            return True
        
        if len(self.abbreviations[abbr]) > 1:
            return False
        
        return word in self.abbreviations[abbr] 

    def getAbbreviation(self, word: str) -> str:
        if len(word) <= 2:
            return word
        
        return word[0] + str(len(word) - 2) + word[-1]


obj = ValidWordAbbr(["deer", "door", "cake", "card", "it", "a", "a"])
print(obj.isUnique("dear"))
print(obj.isUnique("cart"))
print(obj.isUnique("cane"))
print(obj.isUnique("make"))
print(obj.isUnique("cake"))
print(obj.isUnique("it"))
print(obj.isUnique("a"))