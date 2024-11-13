class Calculator:

    def __init__(self):
        self.result = 0

    def add(self, num1, num2):
        return num1 + num2

    def divide(self,x, y):
        return x / y

    def multiply(self, a, b):
        result = a * b
        return result
    
    def subtract(self, a, b):
        return a - b    # Logic error: subtracts in wrong order
    
    def power(self, x, y):
        return x ** y

# Example usage with errors
calc = Calculator()
print(calc.add(2,2))          # Will fail
print(calc.divide(10, 10))      # Will cause division by zero
print(calc.multiply(4, 2))     # Will fail due to undefined variable
print(calc.subtract(5, 3))     # Will give incorrect result
print(calc.power(2, 3))         # Will fail due to syntax 