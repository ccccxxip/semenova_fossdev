#TODO make test to obey principles

import pytest 

from ndfl import calculate_ndfl

def test_ndfl_tier_1_basic():
    assert calculate_ndfl(2000000) == 260000
def test_ndfl_tier_2_basic():
    assert calculate_ndfl(4000000) == 552000
def test_ndfl_tier_3_basic():
    assert calculate_ndfl(10000000) == 1602000
def test_ndfl_tier_4_basic():
    assert calculate_ndfl(30000000) == 5402000
def test_ndfl_tier_5_basic():
    assert calculate_ndfl(60_000_000) == 11_602_000

@pytest.mark.xfail
def test_ndfl_fails_negative_income():
    calculate_ndfl(-1000)