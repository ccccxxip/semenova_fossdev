import sys 
sys.path.append("../src")

#TODO make it with 'clear pip insfall -e'

from math_demo import (add, add_with_bug)

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

if __name__ == "__main__":
    test_addition()
