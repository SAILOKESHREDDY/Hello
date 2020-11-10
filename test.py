from calculator import calculator
import pytest

def test_cases():
    assert(calculator.add(5,6)==11)
    assert(calculator.sub(15,3)==12)
    assert(calculator.mul(20,20)==400)
    assert(calculator.div(100,5)==20)
    assert(calculator.mod(4,6)==4)

test_cases()
