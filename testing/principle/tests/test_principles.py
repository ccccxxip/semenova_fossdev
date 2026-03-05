import sys 
sys.path.append('testing/principle/src')

#TODO make it with 'clear pip insfall -e'

from math_demo import (add, add_with_bug, calculator_tax_bugged, calculator_tax)

def test_addition():
    assert add(2, 2) == 4
    assert add(0, 0) == 0
    assert add(7, 6) == 13
    print("test ADDIOTION PASSED")

def test_addition_with_bug():
    assert add_with_bug(2, 2) == 4
    assert add_with_bug(0, 0) == 0
    # finally we found data that make test reliable
    # assert add_with_bug(7, 6) == 13 # will fail here 
    print("test bugged addition passed")

def test_addition_duplicate():
    assert add(6, 7) == 6 + 7
    print("test duplacate addition passed")
    
def test_additin_overkill():
    for i in range(0, 2 ** 32):
        for j in range(0, 2 ** 32):
            assert add(i, j) == i + j 
            assert add(-i, j) == -i + j
            assert add(-i, -j) == -i -j
            assert add(i, -j) == i -j

def test_addition_clussters():
    assert add(7, 6) == 13
    assert add(0, 6) == 6
    assert add(10, -11) == -1
    assert add(-10, -11) == -21
    assert add(-5, 0) == -5
    assert add(0, -2) == -2
    print("test clusters passed")

def test_tax_calculator_pesticide():
    # only integers don't allow some test cases 
    assert calculator_tax(1000) == 150
    assert calculator_tax(100) == 15
    assert calculator_tax(10) ==  1.5
    assert calculator_tax(1) == 0.15
    assert calculator_tax(234) == 35.1
    print("test unbugged calculator passed")
    # assert calculator_tax_bugged(2.34) == 0.35

def test_tax_calculator():
    assert calculator_tax_bugged(1000) == 150
    assert calculator_tax_bugged(100) == 15 
    assert calculator_tax_bugged(10) ==  1.5
    assert calculator_tax_bugged(1) == 0.15
    assert calculator_tax_bugged(234) == 35.1
    print("test calculator tax passed")
    # float may 
    # assert calculator_tax_bugged(2.34) == 0.35

def test_negative_income():
    try:
        calculator_tax(-100)
    except ValueError as e:
        print("test negative income passed")

if __name__ == "__main__":
    test_addition()
    test_addition_with_bug()
    test_addition_duplicate()
    # test_additin_overkill()
    test_addition_clussters()
    test_tax_calculator()
    test_tax_calculator()
    test_negative_income()

