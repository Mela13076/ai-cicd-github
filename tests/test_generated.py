import pytest

# Tests for add from app.py
```python
import pytest

# Assuming the add function is available in the same scope or imported from a module
# For this example, we'll redefine it here for clarity.
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


def test_add_positive_integers():
    """Test addition with two positive integers."""
    assert add(1, 2) == 3
    assert add(100, 200) == 300
    assert add(5, 10) == 15


def test_add_negative_integers():
    """Test addition with two negative integers."""
    assert add(-1, -2) == -3
    assert add(-10, -5) == -15


def test_add_mixed_positive_and_negative():
    """Test addition with a mix of positive and negative integers."""
    assert add(5, -2) == 3
    assert add(-2, 5) == 3
    assert add(-10, 5) == -5
    assert add(5, -10) == -5


def test_add_with_zero():
    """Test addition involving zero."""
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, -5) == -5
    assert add(-5, 0) == -5
    assert add(0, 0) == 0


def test_add_with_none_values_raises_type_error():
    """Test that passing None values raises a TypeError, respecting type hints."""
    with pytest.raises(TypeError):
        add(1, None)
    with pytest.raises(TypeError):
        add(None, 2)
    with pytest.raises(TypeError):
        add(None, None)

```

# Tests for is_even from app.py
```python
import pytest

# The function to be tested (assuming it's in the same file or imported)
def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def test_is_even_positive_even_number():
    """Test with a standard positive even integer."""
    assert is_even(4) is True

def test_is_even_positive_odd_number():
    """Test with a standard positive odd integer."""
    assert is_even(7) is False

def test_is_even_zero():
    """Test with zero, which is considered an even number."""
    assert is_even(0) is True

def test_is_even_negative_even_number():
    """Test with a negative even integer."""
    assert is_even(-6) is True

def test_is_even_with_none_input_raises_type_error():
    """
    Test with None as input, which is an invalid type for the function,
    expecting a TypeError.
    """
    with pytest.raises(TypeError):
        is_even(None)

def test_is_even_with_float_input_raises_type_error_or_behaves_as_expected():
    """
    Test with a float input. While the type hint specifies int, Python's
    modulo operator (%) works with floats. Depending on strictness, one might
    expect a TypeError, but the current implementation would process it.
    Here we test the behavior when a float is passed.
    """
    # For an even float like 4.0
    assert is_even(4.0) is True
    # For an odd float like 3.0 (3.0 % 2 == 1.0)
    assert is_even(3.0) is False
    # For a non-integer float like 3.5 (3.5 % 2 == 1.5)
    assert is_even(3.5) is False
```

# Tests for reverse_string from app.py
```python
import pytest

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

def test_reverse_string_basic_alphanumeric():
    """Test reversing a standard alphanumeric string."""
    assert reverse_string("hello") == "olleh"
    assert reverse_string("12345") == "54321"

def test_reverse_string_empty_input():
    """Test reversing an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_with_spaces_and_special_chars():
    """Test reversing a string containing spaces and special characters."""
    assert reverse_string(" hello world! ") == " !dlrow olleh "
    assert reverse_string("a-b_c d!") == "!d c_b-a"

def test_reverse_string_single_character():
    """Test reversing a string with a single character."""
    assert reverse_string("a") == "a"
    assert reverse_string("7") == "7"

def test_reverse_string_with_none_input_raises_type_error():
    """Test that passing None to the function raises a TypeError."""
    with pytest.raises(TypeError):
        reverse_string(None)
```

# Tests for factorial from app.py
```python
import pytest

def factorial(n):
    """Calculate the factorial of n."""
    if n < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def test_factorial_positive_number():
    """Test factorial with a positive integer."""
    assert factorial(5) == 120
    assert factorial(3) == 6

def test_factorial_zero():
    """Test factorial for n = 0 (edge case)."""
    assert factorial(0) == 1

def test_factorial_one():
    """Test factorial for n = 1 (edge case)."""
    assert factorial(1) == 1

def test_factorial_negative_number_raises_value_error():
    """Test that factorial raises ValueError for negative numbers."""
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        factorial(-1)
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        factorial(-5)

def test_factorial_large_number():
    """Test factorial with a slightly larger positive integer."""
    assert factorial(7) == 5040
```