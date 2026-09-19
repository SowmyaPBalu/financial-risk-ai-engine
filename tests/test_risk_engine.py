import pytest
from src.risk_engine.main import calculate_risk_score

def test_calculate_risk_score():
    result = calculate_risk_score(100000, 30000)

    assert result == 0.3

def test_calculate_risk_score_rejects_zero_income():
    with pytest.raises(ValueError):
        calculate_risk_score(0, 30000)