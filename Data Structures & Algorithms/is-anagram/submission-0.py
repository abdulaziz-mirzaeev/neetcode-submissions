class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        letters = {}
        for char in s:
            if char in letters:
                letters[char] += 1
            else:
                letters[char] = 1
        
        lettersT = {}
        for char in t:
            if not char in letters:
                return False
            
            if char in lettersT:
                lettersT[char] += 1
            else:
                lettersT[char] = 1
        
        if len(letters.keys()) != len(lettersT.keys()):
            return False
        
        for key in letters.keys():
            if letters[key] != lettersT[key]:
                return False
        
        return True
