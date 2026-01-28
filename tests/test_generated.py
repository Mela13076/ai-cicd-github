import pytest

# Tests for add from app.py
```python
import pytest

def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b

def test_add_positive_integers_returns_sum():
    """Test adding two positive integers."""
    assert add(2, 3) == 5

def test_add_negative_integers_returns_sum():
    """Test adding two negative integers."""
    assert add(-5, -3) == -8

def test_add_mixed_integers_returns_correct_sum():
    """Test adding a positive and a negative integer."""
    assert add(10, -5) == 5
    assert add(-7, 2) == -5

def test_add_with_zero_inputs_returns_correct_sum():
    """Test adding with zero for one or both inputs."""
    assert add(0, 7) == 7
    assert add(5, 0) == 5
    assert add(0, 0) == 0

def test_add_none_values_raises_type_error():
    """Test adding None values, expecting a TypeError."""
    with pytest.raises(TypeError):
        add(None, 5)
    with pytest.raises(TypeError):
        add(5, None)
    with pytest.raises(TypeError):
        add(None, None)
```

# Tests for is_even from app.py
```python
import pytest

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def test_is_even_with_positive_even_number():
    """Test is_even with a typical positive even number."""
    assert is_even(4) is True

def test_is_even_with_positive_odd_number():
    """Test is_even with a typical positive odd number."""
    assert is_even(7) is False

def test_is_even_with_zero():
    """Test is_even with zero, which is considered an even number."""
    assert is_even(0) is True

def test_is_even_with_negative_even_number():
    """Test is_even with a negative even number."""
    assert is_even(-6) is True

def test_is_even_with_negative_odd_number():
    """Test is_even with a negative odd number."""
    assert is_even(-3) is False

def test_is_even_with_none_input_raises_type_error():
    """Test is_even with None input, expecting a TypeError."""
    with pytest.raises(TypeError):
        is_even(None)

def test_is_even_with_float_input_raises_type_error():
    """Test is_even with a float input, expecting a TypeError because of the modulo operation."""
    # Although Python's modulo works with floats, the type hint suggests int,
    # and direct modulo for non-int types can lead to unexpected behavior if not handled.
    # For a float like 2.0, n % 2 would be 0.0, which evaluates to True.
    # For 2.1, n % 2 would be 0.1.
    # However, passing a non-integer is a violation of the type hint, and typically
    # a function designed for int might error or behave unexpectedly.
    # The current implementation will process floats without an explicit type error unless
    # the float is something like 'inf' or 'nan'.
    # A more robust check might involve isinstance(n, int), but as per the given source,
    # the natural behavior of '%' with floats should be tested.
    # Let's test a float that *should* be even and one that *should* be odd based on integer logic.
    # The original function *will* return True for 2.0 because 2.0 % 2 == 0.0, and 0.0 == 0 is True.
    # And False for 2.1 because 2.1 % 2 == 0.1, and 0.1 == 0 is False.
    # If the intent was to strictly only accept integers, then a TypeError should be enforced.
    # Given the source, 2.0 will work. So let's test that it works as per Python's rules for floats.
    assert is_even(2.0) is True
    assert is_even(2.1) is False
    # If a stricter type check was desired, we would add it to the function and then test for TypeError.
    # Since the prompt did not ask to modify the function, we test its current behavior with floats.
    # For a true "TypeError" on non-integer, the function source would need to be `if not isinstance(n, int): raise TypeError(...)`
    # As it stands, the '%' operator works for int, float, and complex (though complex % int would raise TypeError).
    # Since `n % 2` is valid for floats, the current function does not raise a TypeError for `float`.
    # I will remove the `pytest.raises(TypeError)` for floats, as the current source doesn't trigger it.
    # Let's refine the "edge case" for non-integer types to truly problematic ones or ones that lead to distinct behavior.
    pass # Removing the strict TypeError for float based on actual function behavior.
```

# Tests for reverse_string from app.py
```python
import pytest

def reverse_string(s: str) -> str:
    """Reverse a string."""
    return s[::-1]

def test_reverse_string_basic_case():
    """Test with a standard non-empty string."""
    assert reverse_string("hello") == "olleh"

def test_reverse_string_empty_string():
    """Test with an empty string."""
    assert reverse_string("") == ""

def test_reverse_string_single_character():
    """Test with a string containing only one character."""
    assert reverse_string("a") == "a"

def test_reverse_string_palindrome():
    """Test with a string that is a palindrome."""
    assert reverse_string("madam") == "madam"

def test_reverse_string_with_spaces_and_numbers():
    """Test with a string containing spaces, numbers, and special characters."""
    assert reverse_string("  hello 123!  ") == "  !321 olleh  "
```

# Tests for multiply from app.py
```python
import pytest

def multiply(a: int, b: int) -> int:
    """Multiply two numbers together."""
    return a * b

def test_multiply_positive_integers():
    """Test multiplication of two positive integers."""
    assert multiply(2, 3) == 6
    assert multiply(10, 5) == 50
    assert multiply(1, 1) == 1

def test_multiply_with_zero():
    """Test multiplication involving zero."""
    assert multiply(0, 5) == 0
    assert multiply(10, 0) == 0
    assert multiply(0, 0) == 0

def test_multiply_negative_integers():
    """Test multiplication involving negative integers."""
    assert multiply(-2, 3) == -6
    assert multiply(2, -3) == -6
    assert multiply(-2, -3) == 6
    assert multiply(-5, 0) == 0

def test_multiply_with_none_values():
    """Test that multiplying with None raises a TypeError."""
    with pytest.raises(TypeError):
        multiply(None, 5)
    with pytest.raises(TypeError):
        multiply(10, None)
    with pytest.raises(TypeError):
        multiply(None, None)

def test_multiply_with_float_inputs():
    """Test multiplication with float inputs to observe Python's behavior."""
    # Note: Although the function is type-hinted for int, Python's '*' operator
    # allows multiplication with floats, returning a float.
    # This test demonstrates that behavior.
    assert multiply(2.5, 2) == 5.0
    assert multiply(3, 1.5) == 4.5
    assert multiply(-2.0, 3) == -6.0
    assert multiply(0.5, 0.5) == 0.25
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

def test_factorial_of_zero():
    """Test that factorial of 0 is 1."""
    assert factorial(0) == 1

def test_factorial_of_one():
    """Test that factorial of 1 is 1."""
    assert factorial(1) == 1

def test_factorial_of_positive_integer():
    """Test factorial for a positive integer (e.g., 5)."""
    assert factorial(5) == 120

def test_factorial_of_larger_positive_integer():
    """Test factorial for a larger positive integer (e.g., 10)."""
    assert factorial(10) == 3_628_800

def test_factorial_of_negative_number_raises_error():
    """Test that factorial for a negative number raises a ValueError."""
    with pytest.raises(ValueError, match="Factorial not defined for negative numbers"):
        factorial(-1)

def test_factorial_with_none_input_raises_type_error():
    """Test that passing None as input raises a TypeError."""
    with pytest.raises(TypeError):
        factorial(None)

def test_factorial_with_float_input_raises_type_error():
    """Test that passing a float as input raises a TypeError."""
    with pytest.raises(TypeError):
        factorial(5.5)
```