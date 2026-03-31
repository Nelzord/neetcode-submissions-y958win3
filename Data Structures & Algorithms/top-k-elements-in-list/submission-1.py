class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        collection = {}
        for i in nums:
            if i in collection.keys():
                collection[i] += 1
            else:
                collection[i] = 1


        sortedCollection = sorted(collection.items(), key=lambda item: item[1])

        sortedCollection.reverse()
        print(sortedCollection)
        arrayResult = []
        for i in range(k):
            arrayResult.append(sortedCollection[i][0])
        
        return arrayResult


        