import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = []
        for i in stones:
            heapq.heappush(heap, -i)

        while len(heap) > 1:
            val1 = -heapq.heappop(heap)
            val2 = -heapq.heappop(heap)

            if val1 == val2:
                continue 
            else:
                newWeight = val2 - val1
                heapq.heappush(heap, newWeight)

        if len(heap) == 0:
            return 0
        else:
            return -heapq.heappop(heap)

        print(max_val)