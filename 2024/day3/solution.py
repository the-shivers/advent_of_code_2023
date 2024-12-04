# import re

# input_txt = 'advent_of_code/2024/day3/input.txt'
# with open(input_txt) as file:
#     input_str = ''.join(line.strip() for line in file)

# # Part 1
# def get_products(s: str) -> int:
#     matches = re.findall(r'mul\((\d+),(\d+)\)', s)
#     return sum(int(pair[0]) * int(pair[1]) for pair in matches)

# print(f'Part 1: {get_products(input_str)}')

# # Part 2
# substrs = re.findall(r'^.*?don\'t\(\)|do\(\).*?(?:don\'t\(\)|$)', input_str)

# print(f'Part 2: {sum(get_products(s) for s in substrs)}')

import re

part1 = part2 = 0
is_valid = True

for a, b, do, dont in re.findall(
    r"(?<=mul\()(\d{1,3}),(\d{1,3})(?=\))|(do\(\))|(don't\(\))",
    open('advent_of_code/2024/day3/input.txt').read(),
):
    if do:
        is_valid = True
    elif dont:
        is_valid = False
    else:
        product = int(a) * int(b)
        part1 += product
        part2 += product * is_valid

print(part1)
print(part2)