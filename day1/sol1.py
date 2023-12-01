import re

nums = []

with open("input", 'r') as f:
    for line in f.readlines():
      digits = re.findall(r'\d', line)
      nums.append(int(digits[0] + digits[-1]))

print(sum(nums))