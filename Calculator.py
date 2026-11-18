def calculation(x, y, operation):
    if operation == "+":
        return x + y
    elif operation == "-":
        return x - y
    elif operation == "*":
        return x * y
    elif operation == "/":
        if y == 0:
            return "Error Division by zero is not alowed."
        return x/ y 
    elif operation == "^":
        return x ** y

def ask_number():
      while True:
        try:
            return float(input("Number: "))
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
	

		x = ask_number()

		operation = input("Operation:")
		

		if operation not in ["+", "-", "*", "/", "^", "="]:
			print("Error: Invalid operation. Please use +, -, *, /, or ^.")
			operation = input("Operation:")

		while operation in ["+", "-", "*", "/", "^"]:
			y = ask_number()
			
			z = calculation(x, y, operation)
    		
			operation = input("Operation: ")
			while operation not in ["+", "-", "*", "/", "^", "="]:
				print("Error: Invalid operation. Please use +, -, *, /, or ^.")
				operation = input("Operation:")


		print ("Result:", z )
    	
		Calculater_on = input("Do you want to perform another calculation? (yes/no): ")
		if Calculater_on == "no":
					print("Thank you for using the calculator. Goodbye!")
        