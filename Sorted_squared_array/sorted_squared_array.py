def sortedSquaredArray(array):
    temp = len(array) * [0]
    start = 0
    end = len(array) - 1
    for i in reversed(range(len(array))):
        if abs(array[start]) > abs(array[end]):
            temp[i] = array[start] * array[start]
            start += 1
        else:
            temp[i] = array[end] * array[end]
            end -= 1
        
    return temp
