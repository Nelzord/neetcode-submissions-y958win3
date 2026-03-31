class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        totalProduct = 0
        firstNumber = True
        nonZeroProduct = 0
        zeroCounter = 0
        for i in nums:
            if i == 0:
                zeroCounter = zeroCounter + 1
            if firstNumber == True:
                totalProduct += i
                firstNumber = False
                nonZeroProduct += i
            else:
                if i != 0:
                    nonZeroProduct *= i
                totalProduct = totalProduct * i
        

        print(totalProduct)
        resultArray = []
        for i in nums:
            if i == 0:
                if zeroCounter == 1:
                    resultArray.append(nonZeroProduct)
                else:
                    resultArray.append(totalProduct)
            else:
                resultArray.append(int(totalProduct / i))

        return resultArray