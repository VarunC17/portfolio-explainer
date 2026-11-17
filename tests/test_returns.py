import pytest
from src.returns import daily_return
from src.returns import format_pct


def test_daily_return_up():
    assert daily_return(100, 102.5) == pytest.approx(0.025)

def test_daily_return_down():
    assert daily_return(200, 150) == pytest.approx(-0.25)

def test_daily_return_middle():
    assert daily_return(50, 50) == pytest.approx(0.0)

def test_format_pct_positive():
    assert format_pct(0.025) == "+2.50%"

def test_format_pct_negative():
    assert format_pct(-0.25) == "-25.00%"

def test_format_pct_zero():
    assert format_pct(0.0) == "+0.00%"