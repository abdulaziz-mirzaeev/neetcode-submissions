class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = list(filter(lambda char: char.isalnum(), s.lower()))
        left, right = 0, len(filtered) - 1

        while right >= left:
            if filtered[left] != filtered[right]:
                return False
            
            left += 1
            right -= 1
        
        return True