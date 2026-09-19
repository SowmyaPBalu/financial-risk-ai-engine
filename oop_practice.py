class Applicant:
    def __init__(self, income, debt):
        self.income = income
        self.debt = debt

    def debt_ratio(self):
        return self.debt/self.income

    def risk_decision(self):
        if self.debt_ratio() < 0.30:
            return "LOW_RISK"
        elif self.debt_ratio() <0.50:
            return "MEDIUM_RISK"
        else:
            return "HIGH_RISK"

applicant1 = Applicant(100000, 30000)
print(f"applicant1's income:{applicant1.income}")
print(f"applicant1's debt:{applicant1.debt}")
print(f"applicant1's debt_ratio:{applicant1.debt_ratio()}")
print(f"applicant1's decision: {applicant1.risk_decision()}")

applicant2 = Applicant(200000, 50000)
print(f"applicant2's debt_ratio:{applicant2.debt_ratio()}")
print(f"applicant2's decision: {applicant2.risk_decision()}")

# INHERTANCE
class BusinessApplicant(Applicant):
    def business_risk_check(self):
        if self.debt_ratio() < 0.40:
            return "BUSINESS_RISK_ACCEPTABLE"
        else:
            return "BUSINESS_RISK_REVIEW"

applicant1 = BusinessApplicant(200000, 50000)
print(f"Inherited debt_ratio: {applicant1.debt_ratio()}")
print(f"Inherited risk_check: {applicant1.business_risk_check()}")
