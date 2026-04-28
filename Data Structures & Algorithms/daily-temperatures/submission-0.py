class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stacker = []
        

        for i in range(n):
            while stacker and temperatures[i] > temperatures[stacker[-1]]:
                idx = stacker.pop()
                res[idx] = i - idx
            stacker.append(i)

        return res


