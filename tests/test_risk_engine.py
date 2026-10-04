import pytest
from src.risk_engine.main import calculate_risk_score, get_credit_score

@pytest.mark.unit
def test_calculate_risk_score():
    result = calculate_risk_score(100000, 30000)

    assert result == 0.3

def test_calculate_risk_score_rejects_zero_income():
    with pytest.raises(ValueError
                       , match="Income must be greater than zero"):
        calculate_risk_score(0, 30000)

@pytest.mark.unit
def test_calculate_risk_score_rejects_negative_debt():
    with pytest.raises(ValueError
                       , match="Debt cannot be negative"):
        calculate_risk_score(100000, -30000)

@pytest.mark.unit
def test_risk_score_for_high_debt():
    result = calculate_risk_score(100000, 50000)
    assert result == 0.5

# Parametrization concept
@pytest.mark.parametrize(
    "income, debt, expected",
    [
        (100000, 30000, 0.3),
        (100000, 50000, 0.5),
        (200000, 50000, 0.25),
        (80000, 40000, 0.5),
    ],
)
def test_risk_score_multiple_inputs(income, debt, expected):
    result = calculate_risk_score(income, debt)
    assert result == expected

# Fixture concept - A fixture is basically reusable test setup/data.
"""
A fixture isn't necessarily "test data only."
It can also create/setup things such as:

database connections
API clients
temporary files
model objects
test datasets
configuration
mock services

"""
def test_calculate_risk_score(applicant):
    result = calculate_risk_score(
        applicant["income"],
        applicant["debt"]
    )
    assert result == 0.3

# Not necessarily call the fucntion rather just give the fixture called applicant to above test
@pytest.fixture
def applicant():
    return {
        "income": 100000,
        "debt": 30000,
    }

@pytest.fixture(scope="function")
def applicant():
    return {
        "income": 100000,
        "debt": 30000,
    }

# # Edge case
# # This is useful because 0 is a valid value for debt, while 0 is not a valid value for income.
# def test_risk_score_with_zero_debt():
#     result = calculate_risk_score(100000, 0)
#     assert result == 0.0

# # -ve income
# def test_calculate_risk_score_rejects_negative_income():
#     with pytest.raises(
#         ValueError,
#         match="Income must be greater than zero"
#     ):
#         calculate_risk_score(-10000, 30000)

"""
parametrize:-

Instead of:
test_zero_income()
test_negative_income()

we have:
test_invalid_income(income)
"""
@pytest.mark.parametrize(
    "income",
    [
        0,
        -10000,
    ],
)
def test_calculate_risk_score_rejects_invalid_income(income):
    with pytest.raises(
        ValueError,
        match="Income must be greater than zero"
    ):
        calculate_risk_score(income, 30000)

# Mocking - test is fast, deterministic, and independent of external systems.
def test_get_credit_score():
    result = get_credit_score("CUST001")
    assert result == 750

"""
unit tests        → fast
integration tests → slower
API tests         → slower
ML tests          → potentially expensive
"""
from unittest.mock import Mock
@pytest.mark.unit
def test_get_credit_score():
    mock_database = Mock()
    mock_database.get_score.return_value = 800

    result = get_credit_score("CUST001", mock_database)

    assert result == 800
# It can detect incorrect interaction between components, not just incorrect final results.
    mock_database.get_score.assert_called_once_with("CUST001")
