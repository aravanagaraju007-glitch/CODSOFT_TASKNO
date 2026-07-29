def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b

def modulus(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a % b

def power(a, b):
    return a ** b

def floor_division(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a // b

def main():
    print("=" * 40)
    print("       SIMPLE CALCULATOR")
    print("=" * 40)

    while True:
        try:
            num1 = float(input("\nEnter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("Invalid input! Please enter numeric values.")
            continue

        print("\nChoose Operation")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Modulus (%)")
        print("6. Power (**)")
        print("7. Floor Division (//)")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            print("Result =", add(num1, num2))

        elif choice == "2":
            print("Result =", subtract(num1, num2))

        elif choice == "3":
            print("Result =", multiply(num1, num2))

        elif choice == "4":
            print("Result =", divide(num1, num2))

        elif choice == "5":
            print("Result =", modulus(num1, num2))

        elif choice == "6":
            print("Result =", power(num1, num2))

        elif choice == "7":
            print("Result =", floor_division(num1, num2))

        elif choice == "8":
            print("\nThank you for using the Calculator!")
            break

        else:
            print("Invalid choice! Please select between 1 and 8.")
            continue

        again = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()

        if again != "yes":
            print("\nThank you for using the Calculator!")
            break


if __name__ == "__main__":
    main()
