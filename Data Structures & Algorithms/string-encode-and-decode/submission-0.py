class Solution:

    def encode(self, strs: List[str]) -> str:
        encodedString = ""
        for i in strs:
            encodedString += i + "SPACE"

        return encodedString

    def decode(self, s: str) -> List[str]:

        splittedList = s.split("SPACE")
        splittedList = splittedList[:len(splittedList) - 1]
        return splittedList