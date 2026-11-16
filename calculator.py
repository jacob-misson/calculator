Calculater_on = input("Do you want to perform a calculation? (yes/no): ")
if Calculater_on not in ["yes", "no"]:	
	print("Error: Invalid input. Please enter 'yes' or 'no'.")
	Calculater_on = input("Do you want to perform a calculation? (yes/no): ")
if Calculater_on == "no":
		print("Thank you for using the calculator. Goodbye!")
if Calculater_on == "yes":	
	while Calculater_on == "yes":
	

		x = input("First number:")
		while not isinstance(x, int):
			print("Error: Invalid input. Please enter a valid number.")
			x = input("First number:")
		else:
			x = int(x)

		operation = input("Operation:")
		

		if operation not in ["+", "-", "*", "/", "^", "="]:
			print("Error: Invalid operation. Please use +, -, *, /, or ^.")
			operation = input("Operation:")

		while operation in ["+", "-", "*", "/", "^"]:
			y = input("Next number:")
			while not isinstance(y, int):
				print("Error: Invalid input. Please enter a valid number.")
				y = input("Next number:")
			else:
				y = int(y)
			
			if operation == "+":
				x = x + y
				
			if operation == "-":
				x = x - y
			
			if operation == "*":
				x = x * y
     		
			if operation == "/":
				if y == 0:
					print("Error: Division by zero is not allowed.")	
				else:
					x = x  / y
			if operation == "^":
				x = x ** y
    		
			operation = input("Operation: ")
			while operation not in ["+", "-", "*", "/", "^", "="]:
				print("Error: Invalid operation. Please use +, -, *, /, or ^.")
				operation = input("Operation:")
		if operation == "=":
			print ("Result:", x)
			Calculater_on = input("Do you want to perform another calculation? (yes/no): ")
			if Calculater_on == "no":
	 			print("Thank you for using the calculator. Goodbye!")
