# A risk decision engine that takes an applicant's information and produces a decision.
def calculate_risk_score(income: float, debt: float) -> float:
    if income <= 0:
        raise ValueError("Income must be greater than zero")
    if debt < 0:
        raise ValueError("Debt cannot be negative")

    debt_ratio = debt / income
    return debt_ratio
