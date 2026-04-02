class Solution:
    def isPalindrome(self, s: str) -> bool:

        aList = []
        for i in s:
            if i.isalpha() or i.isnumeric():
                aList.append(i.lower())

        lPtr = 0 
        rPtr = len(aList) - 1
        while lPtr <= rPtr:
            if aList[lPtr] == aList[rPtr]:
                lPtr = lPtr + 1
                rPtr = rPtr - 1
                continue
            else:
                return False
        return True