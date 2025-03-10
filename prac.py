

numbers = [0, -31, -24, -10, 1, 9]
answer = numbers[0] * numbers[1]

for i in range(0,len(numbers)-1):
    for j in range(i+1,len(numbers)):
        if answer < numbers[i] * numbers[j]:
            answer = numbers[i] * numbers[j]

print(answer)