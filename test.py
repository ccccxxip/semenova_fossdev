from script import sum ,devide
def test_sum():
    a = 1
    b = 2
    result = 3
    assert sum(a,b) == result

def test_devide():
    a = 2
    b = 4
    result = 0.5
    assert devide(a,b) == result

def test_division_prohibited():
    try:
        divide([1, 2, 4], [1, 2, 3])
        print("Test-string-division failed")
        assert False
    except ValueError as e:
        print("Test string-division passed")
def test_devide_zero():
    a = 2
    b = 0
    try:
        devide(a,b)
        assert False
    except ValueError as e:
        print("Good")

if name == "main":
    test_sum()
    test_devide()
    test_devide_zero()
