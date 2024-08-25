#bubble sort
def bubbleSort(numberList):
    n = len(numberList)
    #we will travese through all the elements
    for i in range(n):
        #we will traveses to n - i - 1
        for j in range(n - i - 1):
            if numberList[j] > numberList[j+1]:
                numberList[j], numberList[j+1] = numberList[j+1], numberList[j]
    return numberList


if __name__ == "__main__":
    numberList = [64, 34, 25, 12, 22, 11, 90]
    sortedList = bubbleSort(numberList)
    print(f"The sorted list is {sortedList}")