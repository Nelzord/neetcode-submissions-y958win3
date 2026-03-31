class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramList = {}

        finalList = []
        for subAnagram in strs:
            key = tuple(sorted(subAnagram))

            if key not in anagramList.keys():
                anagramList[key] = [subAnagram]
            else:
                anagramList[key].append(subAnagram)

        for i in anagramList.keys():
            finalList.append(anagramList[i])
        return finalList

