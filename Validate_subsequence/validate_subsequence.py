def isValidSubsequence(array, sequence):
    count = 0
    for i in range(len(array)):
        if array[i] == sequence[count]:
            count += 1
        if count == len(sequence):
            return True
    return False
