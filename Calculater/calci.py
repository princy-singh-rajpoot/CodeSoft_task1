
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    else:
        return x / y

def calculator():
    print("Welcome to the Simple Calculator!")
    print("Simple Instruction: You will enter your number's and then you will be asked to choose the operation you want to perform on them.")

    while True:
        try:
            num1 = float(input("\nEnter the first number: "))
            num2 = float(input("Enter the second number: "))

            print("\nOperations:")
            print("1. Addition (+)")
            print("2. Subtraction (-)")
            print("3. Multiplication (*)")
            print("4. Division (/)")

            choice = input("\nEnter the operation number (1/2/3/4): ")

            if choice == '1':
                result = add(num1, num2)
                print(f"\n{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"\n{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"\n{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"\n{num1} / {num2} = {result}")
            else:
                print("Invalid input! Please enter a valid operation number.")

            again = input("\nDo you want to perform another calculation? (yes/no): ").lower()
            if again != 'yes':
                print("\nThank you for using the calculator!")
                break

        except ValueError:
            print("Invalid input! Please enter valid numbers.")
        except Exception as e:
            print(f"Error: {e}")

# Run the calculator
if __name__ == "__main__":
    calculator()
