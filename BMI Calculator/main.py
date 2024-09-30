height = input("\ntype your height: ")
weight = input("\ntype your weight: ")

weight_as_int = int(weight)
height_as_float = float(height)

# Using the exponent operator **
bmi = weight_as_int / height_as_float ** 2
# or using multiplication and PEMDAS
#bmi = weight_as_int / (height_as_float * height_as_float)

bmi_as_int = int(bmi)
print(f"\nYour BMI is: {bmi_as_int}")