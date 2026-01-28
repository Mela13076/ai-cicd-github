import pytest

# Tests for is_even from app.py
```python
import pytest

def is_even(n: int) -> bool:
    """Check if a number is even."""
    return n % 2 == 0

def test_is_even_with_positive_even_number():
    """Test is_even with a positive even integer."""
    assert is_even(4) is True

def test_is_even_with_positive_odd_number():
    """Test is_even with a positive odd integer."""
    assert is_even(7) is False

def test_is_even_with_zero():
    """Test is_even with zero, which is considered an even number."""
    assert is_even(0) is True

def test_is_even_with_negative_even_number():
    """Test is_even with a negative even integer."""
    assert is_even(-6) is True

def test_is_even_with_none_input_raises_type_error():
    """Test is_even with None input, expecting a TypeError."""
    with pytest.raises(TypeError):
        is_even(None)
```

# Tests for is_palindrome from more_utils.py
```python
import pytest

def is_palindrome(text):
    """Check if a string is a palindrome."""
    cleaned = text.lower().replace(" ", "")
    return cleaned == cleaned[::-1]

def test_is_palindrome_standard_true():
    """Test a standard string that is a palindrome."""
    assert is_palindrome("madam") is True

def test_is_palindrome_with_spaces_and_mixed_case_true():
    """Test a palindrome with spaces and mixed case."""
    assert is_palindrome("Race car") is True
    assert is_palindrome("A man a plan a canal Panama") is True

def test_is_palindrome_standard_false():
    """Test a standard string that is not a palindrome."""
    assert is_palindrome("hello") is False
    assert is_palindrome("python") is False

def test_is_palindrome_empty_string():
    """Test with an empty string, which is considered a palindrome."""
    assert is_palindrome("") is True

def test_is_palindrome_single_character():
    """Test with a single character string, which is a palindrome."""
    assert is_palindrome("a") is True
    assert is_palindrome("Z") is True

def test_is_palindrome_only_spaces():
    """Test with a string containing only spaces, which cleans to an empty string and is a palindrome."""
    assert is_palindrome("   ") is True

def test_is_palindrome_none_input_raises_attribute_error():
    """Test that passing None raises an AttributeError."""
    with pytest.raises(AttributeError):
        is_palindrome(None)
```