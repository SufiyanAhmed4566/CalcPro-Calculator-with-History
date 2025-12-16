"""
CALCPRO: Calculator with History
A simple calculator that saves all calculations
"""

# ============================================
# 1. CALCULATOR CLASS (OOP Implementation)
# ============================================

class Calculator:
    def __init__(self):
        self.history = []  # List to store all calculations
        self.total_calculations = 0
    
    def add(self, num1, num2):
        """Add two numbers"""
        result = num1 + num2
        self._save_calculation(num1, num2, "+", result)
        return result
    
    def subtract(self, num1, num2):
        """Subtract two numbers"""
        result = num1 - num2
        self._save_calculation(num1, num2, "-", result)
        return result
    
    def multiply(self, num1, num2):
        """Multiply two numbers"""
        result = num1 * num2
        self._save_calculation(num1, num2, "*", result)
        return result
    
    def divide(self, num1, num2):
        """Divide two numbers"""
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        result = num1 / num2
        self._save_calculation(num1, num2, "/", result)
        return result
    
    def _save_calculation(self, num1, num2, operator, result):
        """Save calculation to history"""
        calculation = f"{num1} {operator} {num2} = {result}"
        self.history.append(calculation)
        self.total_calculations += 1
    
    def show_history(self):
        """Show all previous calculations"""
        if not self.history:
            print("\nNo calculations in history yet!")
            return
        
        print("\n" + "="*40)
        print("📜 CALCULATION HISTORY")
        print("="*40)
        
        for i, calc in enumerate(self.history, 1):
            print(f"{i}. {calc}")
        
        print(f"\nTotal calculations: {self.total_calculations}")
        print("="*40)
    
    def clear_history(self):
        """Clear all calculation history"""
        self.history.clear()
        self.total_calculations = 0
        print("\nHistory cleared successfully!")

# ============================================
# 2. MAIN APPLICATION
# ============================================

def main():
    """Main program function"""
    
    print("\n" + "="*50)
    print("🧮 WELCOME TO CALCPRO CALCULATOR 🧮")
    print("="*50)
    
    # Create calculator object
    calc = Calculator()
    
    while True:
        # Display menu
        print("\n📋 MAIN MENU:")
        print("1. ➕ Add")
        print("2. ➖ Subtract")
        print("3. ✖️  Multiply")
        print("4. ➗ Divide")
        print("5. 📜 View History")
        print("6. 🗑️ Clear History")
        print("7. 🚪 Exit")
        print("-"*30)
        
        try:
            choice = input("Enter your choice (1-7): ").strip()
            
            if choice == "1":
                # Addition
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.add(num1, num2)
                print(f"\n✅ Result: {num1} + {num2} = {result}")
                
            elif choice == "2":
                # Subtraction
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.subtract(num1, num2)
                print(f"\n✅ Result: {num1} - {num2} = {result}")
                
            elif choice == "3":
                # Multiplication
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.multiply(num1, num2)
                print(f"\n✅ Result: {num1} × {num2} = {result}")
                
            elif choice == "4":
                # Division
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                result = calc.divide(num1, num2)
                print(f"\n✅ Result: {num1} ÷ {num2} = {result}")
                
            elif choice == "5":
                # View history
                calc.show_history()
                
            elif choice == "6":
                # Clear history
                calc.clear_history()
                
            elif choice == "7":
                # Exit
                print("\n" + "="*50)
                print("Thank you for using CalcPro Calculator!")
                print(f"Total calculations performed: {calc.total_calculations}")
                print("Goodbye! 👋")
                print("="*50)
                break
                
            else:
                print("\n❌ Invalid choice! Please enter 1-7")
        
        except ValueError:
            print("\n❌ Please enter valid numbers!")
        except KeyboardInterrupt:
            print("\n\n👋 Program stopped by user. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ An error occurred: {e}")

# ============================================
# 3. QUICK DEMO FUNCTION
# ============================================

def quick_demo():
    """Show quick demonstration of calculator"""
    print("\n" + "🔧"*20)
    print("QUICK DEMONSTRATION")
    print("🔧"*20)
    
    calc = Calculator()
    
    # Perform sample calculations
    print("\nPerforming sample calculations...")
    
    results = [
        calc.add(10, 5),
        calc.subtract(20, 8),
        calc.multiply(7, 3),
        calc.divide(15, 3)
    ]
    
    print("\n✅ Sample calculations completed!")
    calc.show_history()
    
    print("\n" + "✅"*20)
    print("Demo completed successfully!")
    print("✅"*20)

# ============================================
# 4. PROGRAM ENTRY POINT
# ============================================

if __name__ == "__main__":
    print("🧮 CALCPRO: Calculator with History 🧮")
    print("Type 'demo' for quick demo or press Enter for main app")
    
    user_input = input("\nYour choice: ").strip().lower()
    
    if user_input == "demo":
        quick_demo()
        main()  # Continue to main app after demo
    else:
        main()
