def selectionSort(ary):
    n = len(ary)
    for i in range(0, n-1):
        minIdx = i
        for k in range(i+1, n):
            if (ary[minIdx] > ary[k]):
                minIdx = k
        tmp = ary[i]
        ary[i] = ary[minIdx]
        ary[minIdx] = tmp

    return ary

moneyAry = [7, 5, 11, 6, 9, 80000, 10, 6, 15, 12]

print('용돈 정렬 전 =>', moneyAry)
moneyAry = selectionSort(moneyAry)
print('용돈 정렬 전 =>', moneyAry)
print('용돈 중앙값 =>', moneyAry[len(moneyAry)//2])