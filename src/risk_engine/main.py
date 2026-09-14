# A risk decision engine that takes an applicant's information and produces a decision.
def calculate_risk_score(income: float, debt: float) -> float:
    debt_ratio = debt / income
    return debt_ratio
