def countCrossInversions(left_sorted, right_sorted):

    print(left_sorted, right_sorted)
    count = 0
    j = 0

    for i in range(len(left_sorted)):
        while j < len(right_sorted) and left_sorted[i] > 2*right_sorted[j]:
            j = j + 1
        count += j
    return count

def stableMerge(left_sorted, right_sorted):
    
    result = []
    i, j = 0, 0

    while i < len(left_sorted) and j < len(right_sorted):
        if left_sorted[i] <= right_sorted[j]:
            result.append(left_sorted[i])
            i = i + 1
        else:
            result.append(right_sorted[j])
            j = j + 1
    
    if i == len(left_sorted):
        while j < len(right_sorted):
            result.append(right_sorted[j])
            j += 1
    elif j == len(right_sorted):
        while i < len(left_sorted):
            result.append(left_sorted[i])
            i += 1

    return result


def strongInversionCount(A):

    n = len(A)
    if n <= 1:
        return 0, A
    
    mid = n//2
    count_left, left_sorted = strongInversionCount(A[:mid])
    count_right, right_sorted = strongInversionCount(A[mid:])

    count_cross = countCrossInversions(left_sorted, right_sorted)
    
    merged = stableMerge(left_sorted, right_sorted)

    return count_left+count_right+count_cross, merged

def main():
    A = list(map(int, input().split()))
    # print(A)

    count, mergedA = strongInversionCount(A)

    print(count, mergedA)

if __name__ == "__main__":
    main()