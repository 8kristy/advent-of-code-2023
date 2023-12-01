import re

nums = []

dictionary = { "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9" }

with open("input", 'r') as f:
    for line in f.readlines():
      digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
      digits = list(map(lambda x: x if x.isdigit() else dictionary[x], digits))
      nums.append(int(digits[0] + digits[-1]))

print(sum(nums))