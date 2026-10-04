# Integration testing
import pytest
from src.risk_engine.main import calculate_risk_score

@pytest.mark.integration
def test_risk_engine_integration():
    result = calculate_risk_score(100000, 30000)

    assert result == 0.3
