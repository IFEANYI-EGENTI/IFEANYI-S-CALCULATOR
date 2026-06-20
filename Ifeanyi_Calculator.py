# -*- coding: utf-8 -*-


# IFEANYI EGENTI
print("IFEANYI'S CALCULATOR")
print()

def calculator(num1, num2):
  operator = input("Please enter an Operator E.g: +, -, *, /: ")
  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
        return "Error: Cannot divide by zero"
    return num1 / num2
  else:
    return "Invalid Operator. Please use +, -, *, /"


while True:
    try:
      first_number = float(input("Please input your first digit: "))
      second_number = float(input("Please input your second digit: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue
    result = calculator(first_number, second_number)
    if isinstance(result, str):
        print(result)
    else:
        print(int(result) if result == int(result) else result)
    print(("Do you want to use Calculator again?"))
    again = input("Input 'yes' to use Calculator again or 'no' to exit: ")
    if again != "yes":
        break