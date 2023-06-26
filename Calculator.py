#Calculator
from art import logo

#Add
def add(n1, n2):
  return n1 + n2

#Subtract
def subtract(n1, n2):
  return n1 - n2

#Multiply
def multiply(n1, n2):
  return n1 * n2

#Divide
def divide(n1, n2):
  return n1 / n2

operations = {
  "+" : add,
  "-" : subtract,
  "*" : multiply,
  "/" : divide,
}
def calculator():             #Calling a function inside itself is known as recursion.
  print(logo)
  
  num1 = float(input("What's the first number?: "))
  
  for symbol in operations:
    print(symbol)
  
  end = False

  # A variable that we define to have one value until some condition is true, in which case you change the variable's value, it is known as flag.
  
  while(not end):
    operation_symbol = input("Pick an operation: ")
    
    num2 = float(input("What's the next number?: "))
    
    calculated_function = operations[operation_symbol]
    answer = calculated_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")
    reply = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
    if(reply == "y"):
      num1 = answer
    else:
      end = True
      calculator()



calculator()
