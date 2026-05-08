
nums = list(map(int, open('17_28108.txt')))
max_n = -500_000_000_000
for n in nums:
    if n > max_n and n % 2 != 0:
        max_n = n
count = 0
min_n = 2000000000000000
for i in range(len(nums) - 4):
    if (nums[i] % max_n == 0 or nums[i + 4] % max_n == 0) and (nums[i] + nums[i + 4]) ** 2 < sum([nums[i + 1] ** 2, nums[i + 2] ** 2, nums[i + 3] ** 2]):
        count += 1
        min_n = min((nums[i] + nums[i + 4]) ** 2, min_n)
print(count, min_n)
