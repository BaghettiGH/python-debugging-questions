# Expected: [2, 4, 6]

nums = [1, 2, 3, 4, 5, 6]
for n in range(0,5):
    if n % 2 != 0:
        nums.remove(n)
print(nums)
