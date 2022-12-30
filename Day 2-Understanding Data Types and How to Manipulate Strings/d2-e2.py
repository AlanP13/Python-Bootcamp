# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
weight_int = int(weight)
height_float = float(height)

# Using the exponent operator **
bmi = weight_int / height_float ** 2

bmi_int = int(bmi)

print(bmi_int)