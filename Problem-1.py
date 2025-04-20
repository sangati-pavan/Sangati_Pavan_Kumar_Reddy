class Calculator:
    def __init__(self, a: float, b: float) :
        self.a = a
        self.b = b

    def operate(self, operation: str) :
        if operation == "add":
            return self.a + self.b
        elif operation == "subtract":
            return self.a - self.b
        elif operation == "multiply":
            return self.a * self.b
        elif operation == "divide":
            return self.a / self.b if self.b != 0 else "Cannot divide by zero"
        else:
            return "Invalid operation"


calc = Calculator(10.0, 5.0)
print(calc.operate("multiply"))  # Output: 50.0
