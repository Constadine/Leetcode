candies = [12, 1, 12]
extraCandies = 10


output = [True if x + extraCandies >= max(candies) else False for x in candies]

print(output)
