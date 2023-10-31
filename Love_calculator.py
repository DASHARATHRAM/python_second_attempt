name1 = input()
name2 = input()
print("The Love Calculator is calculating your score...")

name = name1 + name2
lower_name = name.lower()
t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")
first_digit = t + r + u + e

l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")
second_digit = l + o + v + e

final = str(first_digit) + str(second_digit)
final1 = int(final)
if final1 < 10 or final1 > 90:
    print(f"Your score is {final1}, you go together like coke and mentos.")
elif final1 > 40 and final1 < 50:
    print(f"Your score is {final1}, you are alright together.")
else:
    print(f"Your score is {final1}.")