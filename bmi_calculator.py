weight = float (input("enter the weight in (in kg):"))
height = float(input("enter the height (in meters):"))

bmi = weight/(height**2)

if bmi <18.5:
    category = "underweight"
elif bmi<25:
    category = "normal weight"
elif bmi<30:
    category = "overweight"
else:
    category = "obese"
print(f"\n your BMI is {bmi:.2f})")
print(f"Category:{category}")
