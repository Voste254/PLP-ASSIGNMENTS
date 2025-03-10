num1 = int(input("Enter the first number: "))
operation = input("enter the operation: ")
num2 = int(input("Enter the second number: "))
if(operation =="+"):
  print("The answer is "+ str(num1+num2))
elif(operation == "-"):
  print("The answer is "+ str(num1-num2))
elif(operation == "*"):
  print("The answer is "+ str(num1*num2))
elif(operation == "/"):
  print("The answer is "+ str(num1/num2))
else:
  print("invalid input!!!")