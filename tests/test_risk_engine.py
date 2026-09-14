from src.risk_engine.main import calculate_risk_score

def test_calculate_risk_score():
    result = calculate_risk_score(100000, 30000)

    assert result == 0.3