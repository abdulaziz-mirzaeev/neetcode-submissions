class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        enc_strs = []
        for w in strs:
            prefix = str(len(w)) + '#'
            enc_strs.append(prefix + w)
        
        s = "".join(enc_strs)
        print(s)
        return s
        


    def decode(self, s: str) -> List[str]:
        strs = []
        i = 0
        length = ''
        while i < len(s):
            current = s[i]

            if current == '#':
                length_n = int(length)
                char_from = i+1
                char_to = char_from + length_n
                strs.append(s[char_from:char_to])
                i = char_to
                length = ''
            else:
                length += current
                i += 1
            
        return strs

        
                


    