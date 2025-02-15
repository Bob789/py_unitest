import time

import pytest
import calculator

def test_calculator_add_small():
    # Arrange
    a: int = 2
    b: int = 5
    expected: int = 7

    # Act
    actual: int = calculator.add(a, b)

    # Assert
    assert expected == actual, "small numbers ADD"

def test_calculator_sub_small():
    # Arrange
    a: int = 7
    b: int = 5
    expected: int = 2

    # Act
    actual: int = calculator.minus(a,b)

    # Assert
    assert expected == actual, "small numbers SUB"

def test_calculator_multiply_small():
    # Arrange
    a: int = 7
    b: int = 5
    expected: int = 35

    # Act
    actual: int = calculator.multiply(a,b)

    # Assert
    assert expected == actual, "small numbers MUL"

def test_calculator_power_16():
    # Arrange
    a: int = 4
    b: int = 2
    expected: int = 16

    # Act
    actual: int = calculator.power(a,b)

    # Assert
    assert expected == actual, "small numbers POWER"

def test_calculator_power_9():
    # Arrange
    a: int = 3
    b: int = 2
    expected: int = 9

    # Act
    actual: int = calculator.power(a,b)

    # Assert
    assert expected == actual, "small numbers POWER"

def test_calculator_sqrt_25():
    # Arrange
    a: int = 25
    expected: int = 5

    # Act
    actual: int = calculator.sqrt(a)

    # Assert
    assert expected == actual, "small numbers SQRT"

def test_calculator_sqrt_small_negative():
    with pytest.raises(ValueError) as ex:
        calculator.sqrt(-5)

def test_calculator_factorial_120():
    # Arrange
    a: int = 5
    expected: int = 120

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "small numbers FACTORIAL"

def test_calculator_factorial_24():
    # Arrange
    a: int = 4
    expected: int = 24

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "small numbers FACTORIAL"

def test_calculator_factorial_0():
    # Arrange
    a: int = 0
    expected: int = 1

    # Act
    actual: int = calculator.factorial(a)

    # Assert
    assert expected == actual, "small numbers FACTORIAL"

def test_calculator_factorial_small_negative():
    with pytest.raises(ValueError) as ex:
        calculator.factorial(-3)

