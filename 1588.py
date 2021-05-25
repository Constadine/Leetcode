
arr = [10, 11, 12]

Sum = 0
sliced_array = [[]]

for i in range(len(arr) + 1):
    for j in range(i):
        sliced_array.append(arr[j:i])

for i in range(len(sliced_array)):
    if len(sliced_array[i]) % 2 != 0:
        Sum += sum(sliced_array[i])


print(Sum)

# 2nd way(faster)

total = 0
size = 1
while size <= len(arr):
    for i in range(len(arr)-size+1):
        total += sum(arr[i:i+size])
    size += 2
print(total)
