"""
A simple calculator module with basic arithmetic operations.
"""

class Calculator:
    """A class representing a simple calculator."""
    
    def add(self, a: float, b: float) -> float:
        """
        Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
        """
        return a + b
    
    def subtract(self, a: float, b: float) -> float:
        """
        Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference between a and b
        """
        return a - b
    
    def multiply(self, a: float, b: float) -> float:
        """
        Multiply two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Product of a and b
        """
        return a * b
    
    def divide(self, a: float, b: float) -> float:
        """
        Divide two numbers.
        
        Args:
            a: Dividend
            b: Divisor
            
        Returns:
            Quotient of a divided by b
            
        Raises:
            ValueError: If divisor is zero
        """
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b
    
    def power(self, base: float, exponent: float) -> float:
        """
        Calculate power of a number.
        
        Args:
            base: Base number
            exponent: Exponent
            
        Returns:
            base raised to the power of exponent
        """
        return base ** exponent


def main():
    """Main function to demonstrate calculator usage."""
    calc = Calculator()
    
    print("Calculator Demo:")
    print(f"5 + 3 = {calc.add(5, 3)}")
    print(f"10 - 4 = {calc.subtract(10, 4)}")
    print(f"6 * 7 = {calc.multiply(6, 7)}")
    print(f"20 / 5 = {calc.divide(20, 5)}")
    print(f"2 ^ 8 = {calc.power(2, 8)}")


if __name__ == "__main__":
    main()
    