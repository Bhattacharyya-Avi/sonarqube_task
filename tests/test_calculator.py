"""
Unit tests for the Calculator class.
"""

import pytest
from src.calculator import Calculator


class TestCalculator:
    """Test suite for Calculator class."""
    
    def setup_method(self):
        """Setup method to initialize calculator before each test."""
        self.calc = Calculator()
    
    def test_add(self):
        """Test addition operation."""
        assert self.calc.add(5, 3) == 8
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0
    
    def test_subtract(self):
        """Test subtraction operation."""
        assert self.calc.subtract(10, 4) == 6
        assert self.calc.subtract(5, 5) == 0
        assert self.calc.subtract(0, 5) == -5
    
    def test_multiply(self):
        """Test multiplication operation."""
        assert self.calc.multiply(6, 7) == 42
        assert self.calc.multiply(-3, 4) == -12
        assert self.calc.multiply(0, 10) == 0
    
    def test_divide(self):
        """Test division operation."""
        assert self.calc.divide(20, 5) == 4
        assert self.calc.divide(10, 2) == 5
        assert self.calc.divide(5, 2) == 2.5
    
    def test_divide_by_zero(self):
        """Test division by zero raises ValueError."""
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            self.calc.divide(10, 0)
    
    def test_power(self):
        """Test power operation."""
        assert self.calc.power(2, 8) == 256
        assert self.calc.power(5, 0) == 1
        assert self.calc.power(3, 2) == 9
    
    def test_combined_operations(self):
        """Test combined operations."""
        result = self.calc.add(
            self.calc.multiply(3, 4),
            self.calc.divide(10, 2)
        )
        assert result == 17


if __name__ == "__main__":
    pytest.main([__file__, "-v"])