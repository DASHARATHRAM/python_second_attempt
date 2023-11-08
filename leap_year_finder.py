year = int(input())
if year % 4 == 0:
    print("IT'S A LEAP YEAR")
elif year % 100 == 0:
    print("IT'S A LEAP YEAR")
elif year % 400 == 0:
    print("IT'S A LEAP YEAR")
else:
    print("It's not a leap year")