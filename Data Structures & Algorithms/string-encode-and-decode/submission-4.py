class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedStr = ''
        for i in range(len(strs)):
            encodedStr += str(len(strs[i])) + '#' + strs[i]
        
        return encodedStr

    def decode(self, s: str) -> List[str]:

        decoded = []
        i = 0
        while i < len(s):

            j = i+1
            word = ''
            while s[j] != '#':
                j+=1
            
            length = int("".join(s[i:j]))
            
            decoded.append(s[j+1:j+length+1])

            i = j+length+1
        return decoded
