class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ''
        for word in strs:
            s+=f'{len(word)}#{word}'
        print(s)
        return s
                    
    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        w_end = 0
        while i < len(s):
            if s[i] != '#':
                i+= 1
                continue 
            length = int(s[w_end:i])
            w_end = i+1+length
            decoded.append(s[i+1:i+1+length])
            i = w_end
        return decoded

            