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

# Override
class BusinessApplicant_override(Applicant):
    def risk_decision(self):
        if self.debt_ratio() < 0.40:
            return "RISK_ACCEPTABLE"
        else:
            return "RISK_TO_BE_REVIEWED"

applicant4 = BusinessApplicant_override(200000, 50000)
print(f"Override debt_ratio: {applicant4.debt_ratio()}")
print(f"Override risk_check: {applicant4.risk_decision()}")

# SUPER()
class BusinessApplicant_super(Applicant):
    def risk_decision(self):
        parent_decision = super().risk_decision()
        return parent_decision + " + BUSINESS_CHECK"

applicant5 = BusinessApplicant_super(200000, 50000)
print(f"Super debt_ratio: {applicant5.debt_ratio()}")
print(f"Super risk_check: {applicant5.risk_decision()}")

# COMPOSITION
class RiskAssessment:
    def __init__(self, risk_score):
        self.risk_score = risk_score

    def risk_level(self):
        if self.risk_score < 0.30:
            return "LOW_RISK"
        elif self.risk_score < 0.50:
            return "MEDIUM_RISK"
        else:
            return "HIGH_RISK"

assessment = RiskAssessment(0.25)

print(f"Composition risk_check: {assessment.risk_level()}")

class ApplicantWithAssessment:
    def __init__(self, income, debt):
        self.income = income
        self.debt = debt

        risk_score = debt / income
        self.assessment = RiskAssessment(risk_score)

    def show_risk(self):
        return self.assessment.risk_level()

applicant6 = ApplicantWithAssessment(200000, 50000)

print(f"Income: {applicant6.income}")
print(f"Debt: {applicant6.debt}")
print(f"Risk score: {applicant6.assessment.risk_score}")
print(f"Risk level: {applicant6.show_risk()}")

# TEST
class LoanApplicant(Applicant):
    def __init__(self, income, debt, loan_amount):
        self.income = income
        self.debt = debt
        self.loan_amount = loan_amount

    def risk_decision(self):
        if self.debt_ratio() < 0.24:
            return "RISK_ACCEPTABLE"
        else:
            return "RISK_TO_BE_REVIEWED"

applicant7 = LoanApplicant(200000, 50000, 1000000)

print(f"test_debt_ratio: {applicant7.debt_ratio()}")
print(f"test_override: {applicant7.risk_decision()}")

