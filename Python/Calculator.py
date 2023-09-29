from replit import clear
def add(n1,n2):
  return n1+n2

def subtract(n1,n2):
  return n1-n2

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1/n2

operations = {
"+": add, 
"-": subtract,
"*": multiply,
"/": divide
}

def calculator():
  num1 = float(input("What's the first number?: "))
  num2 = float(input("What's the second number?: "))
  for operation in operations:
    print(operation)
  
  operation_symbol = input("Pick an operation from the line above: ")
  calculation_function = operations[operation_symbol]
  first_answer = calculation_function(num1,num2)
  print(f"{num1} {operation_symbol} {num2} = {first_answer}")
  
  while True:
    to_continue = input(f"Type 'y' to continue calculating with {first_answer}, or type 'n' to exit.:")
    if to_continue == "y":
      operation_symbol = input("Pick an operation from the line above: ")
      num3 = float(input("What's the next number?: "))
      calculation_function = operations[operation_symbol]
      second_answer = calculation_function(first_answer,num3)
      print(f"{first_answer} {operation_symbol} {num3} = {second_answer}")
      first_answer = second_answer
    elif to_continue == "n":
      clear()
      calculator()

calculator()