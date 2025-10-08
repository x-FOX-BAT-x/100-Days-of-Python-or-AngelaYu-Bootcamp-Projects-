#simple BMI calculator
print("Welcome to the BMI calculator. Please answer the below prompts:\n\n")
weight=int(input("Please input your weight in KG:\n\t"))
height=float(input("Please input your height in m:\n\t"))
BMI= weight/(height**2)
print(round(BMI,3))



