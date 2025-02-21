count = 0

def sortQuickN(ary, start, end):
    global count
    if end <= start: return # 재귀호출 종료 조건

    low = start; high = end

    pivot = ary[(low + high) // 2] # 리스트 중간값을 기준으로
    while low <= high:
        while ary[low] < pivot:
            low += 1
        while ary[high] > pivot:
            high -= 1
        if low <= high:
            ary[low], ary[high] = ary[high], ary[low]
            low, high = low + 1, high - 1

            count += 1

    sortQuickN(ary, start, low - 1) # 왼쪽 그룹 다시 정렬(재귀호출)
    sortQuickN(ary, low, end) # 오른쪽 그룹 다시 정렬(재귀호출)

# 변수
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]

# 메인
print('정렬 전 =>', dataAry)
sortQuickN(dataAry, 0, len(dataAry)-1)
print('정렬 후 =>', dataAry)
print('처리횟수:', count)