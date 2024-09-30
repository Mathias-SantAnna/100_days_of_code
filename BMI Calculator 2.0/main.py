height = float(input(f"\nYour height here: "))  # in meters e.g., 1.55
weight = int(input(f"Your weight here: "))  # in kilograms e.g., 72

bmi = weight / (height * height)

if bmi < 18.5:
  print(f"Your BMI is {bmi:.2f}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi:.2f}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi:.2f}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi:.2f}, you are obese.")
else:
  print(f"Your BMI is {bmi:.2f}, you are clinically obese.")