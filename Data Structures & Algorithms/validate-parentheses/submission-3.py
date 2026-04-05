class Solution:
    def isValid(self, s: str) -> bool:
        
        stacker = []

        vals = {")":"(", "}":"{", "]":"["}
        for i in s:
            if i in "([{":
                stacker.append(i)
            if i in ")}]":
                if len(stacker) == 0:
                    return False
                val = stacker.pop()
                if val == vals[i]:
                    continue
                else:
                    return False

        if len(stacker) > 0:
            return False
        return True
