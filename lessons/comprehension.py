prizes = [5, 10, 50, 100, 1000]

dbl_prizes = []
for prize in prizes:
    dbl_prizes.append(2 * prize)

print(dbl_prizes)

# comprehension method
dbl_prizes = [ prize * 2 for prize in prizes]
print(dbl_prizes)

# squaring numbers
nums = list(range(1, 11))
print(nums)

squared_even_nums = []
for num in nums:
    if num ** 2 % 2 == 0:
        squared_even_nums.append(num ** 2)
print(squared_even_nums)

# comprehension method for squaring numbers

squared_even_nums = [num ** 2 for num in nums if (num ** 2) % 2 == 0]
print(squared_even_nums)
