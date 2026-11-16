def add(x, y):
    return x + y  

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y   

def power(x, y):
    return x ** y

def first_number():
    while True:
        x = input("First number: ")
        try:
            return float(x)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

def next_number():
    while True:
        y = input("Next number: ")
        try:
            return float(y)
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")


Calculater_on = input("Do you want to perform a calculation? (yes/no): ")
if Calculater_on not in ["yes", "no"]:	
	print("Error: Invalid input. Please enter 'yes' or 'no'.")
	Calculater_on = input("Do you want to perform a calculation? (yes/no): ")
if Calculater_on == "no":
		print("Thank you for using the calculator. Goodbye!")
if Calculater_on == "yes":	
	while Calculater_on == "yes":
	

		x = first_number()

		operation = input("Operation:")
		

		if operation not in ["+", "-", "*", "/", "^", "="]:
			print("Error: Invalid operation. Please use +, -, *, /, or ^.")
			operation = input("Operation:")

		while operation in ["+", "-", "*", "/", "^"]:
			y = next_number()
			
			if operation == "+":
				x = add(x, y)

			if operation == "-":
				x = subtract(x, y)

			if operation == "*":
				x = multiply(x, y)
     		
			if operation == "/":
				x = divide(x, y)

			if operation == "^":
				x = power(x, y)
    		
			operation = input("Operation: ")
			while operation not in ["+", "-", "*", "/", "^", "="]:
				print("Error: Invalid operation. Please use +, -, *, /, or ^.")
				operation = input("Operation:")
		if operation == "=":
			print ("Result:", x)
			Calculater_on = input("Do you want to perform another calculation? (yes/no): ")
			if Calculater_on == "no":
	 			print("Thank you for using the calculator. Goodbye!")
