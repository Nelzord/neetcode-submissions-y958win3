class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        collection = {}
        collection2 = {}
        for i in s:
            if i not in collection.keys():
                collection[i] = 1
            else:
                collection[i] = collection[i] + 1
        
        for i in t:
            if i not in collection2.keys():
                collection2[i] = 1
            else:
                collection2[i] = collection2[i] + 1

        return collection == collection2