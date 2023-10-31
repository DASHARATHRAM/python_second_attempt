size = input("What size pizza do you want? S, M, or L\n") # What size pizza do you want? S, M, or L
add_pepperoni = input("Do you want pepperoni? Y or N\n") # Do you want pepperoni? Y or N
extra_cheese = input("Do you want extra cheese? Y or N\n")
p = 0
if size == 'S':
    p = 15
    if add_pepperoni == 'Y':
        p += 2
elif size == 'M':
    p = 20
    if add_pepperoni == 'Y':
        p += 3
elif size == 'L':
    p = 25
    if add_pepperoni == 'Y':
        p += 3

if extra_cheese == 'Y':
        p += 1
print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${p}")