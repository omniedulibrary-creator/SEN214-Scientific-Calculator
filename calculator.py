import math

class ScientificCalculator:
    """
    SEN 214: Scientific Calculator
    Author: Engr. C.E.O. PAPPUS
    Architecture: Object-Oriented, Menu-Driven Console Application
    """

    def __init__(self):
        self.is_running = True

    def display_menu(self):
        print("\n" + "="*40)
        print("    STANDARD SCIENTIFIC CALCULATOR")
        print("="*40)
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Power (x^y)")
        print("6. Square Root (√x)")
        print("7. Sine (sin x)")
        print("8. Cosine (cos x)")
        print("9. Tangent (tan x)")
        print("10. Logarithm Base 10 (log x)")
        print("0. Exit")
        print("="*40)

    def get_user_input(self, prompt):
        while True:
            try:
                return float(input(prompt))
            except ValueError:
                print("Error: Please enter a valid standard number.")

    def calculate(self, choice):
        if choice == '0':
            print("Shutting down calculator. Goodbye!")
            self.is_running = False
            return

        if choice in ['1', '2', '3', '4', '5']:
            a = self.get_user_input("Enter first number: ")
            b = self.get_user_input("Enter second number: ")

            if choice == '1':
                print(f"Result: {a} + {b} = {a + b}")
            elif choice == '2':
                print(f"Result: {a} - {b} = {a - b}")
            elif choice == '3':
                print(f"Result: {a} * {b} = {a * b}")
            elif choice == '4':
                if b == 0:
                    print("Error: Division by zero is undefined.")
                else:
                    print(f"Result: {a} / {b} = {a / b}")
            elif choice == '5':
                print(f"Result: {a} ^ {b} = {math.pow(a, b)}")

        elif choice in ['6', '7', '8', '9', '10']:
            a = self.get_user_input("Enter the number/angle: ")

            if choice == '6':
                if a < 0:
                    print("Error: Cannot calculate square root of a negative number.")
                else:
                    print(f"Result: √{a} = {math.sqrt(a)}")
            elif choice == '7':
                print(f"Result: sin({a}°) = {math.sin(math.radians(a)):.4f}")
            elif choice == '8':
                print(f"Result: cos({a}°) = {math.cos(math.radians(a)):.4f}")
            elif choice == '9':
                # Handling the undefined tangent at 90, 270, etc.
                if a % 180 == 90:
                    print("Error: Tangent is undefined for this angle.")
                else:
                    print(f"Result: tan({a}°) = {math.tan(math.radians(a)):.4f}")
            elif choice == '10':
                if a <= 0:
                    print("Error: Logarithm undefined for zero or negative numbers.")
                else:
                    print(f"Result: log10({a}) = {math.log10(a):.4f}")
        else:
            print("Invalid selection. Please choose a valid menu option.")

    def run(self):
        while self.is_running:
            self.display_menu()
            choice = input("Select an operation (0-10): ")
            self.calculate(choice)

if __name__ == "__main__":
    app = ScientificCalculator()
    app.run()
