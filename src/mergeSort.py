from random import shuffle
from time import time

"""
Description: I decided to make this sorting algorithm to make the sentiment
    analysis dictionary program faster. I created this algorithm after I
    modified our original mergeSort algorithm.
"""

def mergeSortDictionary(unsortedDictionary):
    dictKeys = []
    for key in unsortedDictionary:
        dictKeys.append(key)

    return mergeSortDictKeys(dictKeys, unsortedDictionary)


def mergeSortDictKeys(unsortedKeys, dictionary):
    if len(unsortedKeys) <= 1:
        return unsortedKeys
    else:
        middleIndex = int(len(unsortedKeys)/2)

        leftSlice = unsortedKeys[: middleIndex]
        sortedLeft = mergeSortDictKeys(leftSlice, dictionary)
        rightSlice = unsortedKeys[middleIndex:]
        sortedRight = mergeSortDictKeys(rightSlice, dictionary)

        return mergeDictLists(sortedLeft, sortedRight, dictionary)


def mergeDictLists(sortedLeft, sortedRight, dictionary):
    currLeftIndex = 0
    currRightIndex = 0
    newMergedList = []
    notSorted = True
    while notSorted:
        if currLeftIndex >= len(sortedLeft):
            newMergedList = newMergedList + sortedRight[currRightIndex:]
            notSorted = False

        elif currRightIndex >= len(sortedRight): 
            newMergedList = newMergedList + sortedLeft[currLeftIndex:]
            notSorted = False

        else:
            currLeftItem = dictionary[sortedLeft[currLeftIndex]]
            currRightItem = dictionary[sortedRight[currRightIndex]]

            if currLeftItem < currRightItem:
                newMergedList.append(sortedRight[currRightIndex])
                currRightIndex += 1
            else:
                newMergedList.append(sortedLeft[currLeftIndex])
                currLeftIndex += 1
    
    return newMergedList

if __name__ == "__main__":
    D = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6 }
    
    t1 = time()
    print(mergeSortDictionary(D))
    t2 = time()
    print("merge sort time: " + str(t2-t1))

    dcopy = D.copy()
    t1 = time()
    print(sorted(dcopy.items(), key=lambda x:x[1], reverse=True))
    t2 = time()
    print("built-in sort time: " + str(t2-t1))
