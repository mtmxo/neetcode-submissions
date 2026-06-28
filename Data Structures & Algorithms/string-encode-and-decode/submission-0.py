class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""

        for j in range(len(strs)):
            delimiter = str(len(strs[j])).zfill(3)
            encoded += "".join(delimiter) + strs[j]

        return encoded

    def decode(self, s: str) -> List[str]:
        result = []
        delimiter_index = 0
        
        while delimiter_index < len(s):
            word_lenght = int(s[delimiter_index:delimiter_index + 3])
            result.append(s[delimiter_index+3:word_lenght+delimiter_index+3])
            delimiter_index += word_lenght + 3
        
        return result