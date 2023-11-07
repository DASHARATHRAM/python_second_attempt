 # Enter a number between 0 and 1000
target = int(input())
total = 0
for number in range(0, target + 1, 2):
    total += number
print(total)