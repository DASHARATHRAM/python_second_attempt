height = float(input())
weight = int(input())
BMI = weight / (height ** 2)
BMI2 = (round(BMI, 1))
if BMI2 >= 35:
    print(f"Your BMI is {BMI2}, you are clinically obese.")
elif BMI2 >= 30:
    print(f"Your BMI is {BMI2}, you are obese.")
elif BMI2 >= 25:
    print(f"Your BMI is {BMI2}, you are slightly overweight.")
elif BMI2 >= 18.5:
    print(f"Your BMI is {BMI2}, you are normal weight.")
else:
    print(f"Your BMI is {BMI2}, you are underweight.")
    