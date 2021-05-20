nums = [1, 2, 3]
count = 0
for idx, numx in enumerate(nums):
    for idy, numy in enumerate(nums):
        if numx == numy and idx < idy:
            count += 1

print(count)
