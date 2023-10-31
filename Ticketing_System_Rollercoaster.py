height = int(input("what is your height in cm?\n"))
p = 0
if height >= 120:
    print("Can ride")
    age = int(input("what is your age?\n"))
    if age < 12:
        p = 5
        print("Kid's Ticket is $5")
    elif age <= 18:
        p = 7
        print("Big Kids ticket is $7")
    elif age <= 45:
        p = 12
        print("Adult's Ticket is $12")
    else:
        p = 0
        print("You are free my frnd")

    want_photos = input("you wanna snap?\n")
    if want_photos == 'Y':
        p += 3
        print(f"The total bill is ${p}")
else:
    print("Can't Ride")