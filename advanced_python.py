# STR & FLOAT
applicant_name: str = "Sowmya P.B"
age: int = 28
income: float = 100000.0
is_employed: bool = True

print(f"Name of the applicant: {applicant_name}")
print(f"Age of the applicant: {age}")
print(f"Income of the applicant: {income}")
print(f"Is the applicant employed: {is_employed}")

# LIST & DICT
incomes: list[float] = [50000.0, 75000.0, 100000.0]
applicant: dict[str, float] = {
    "income": 100000.0,
    "debt": 30000.0,
    "loan_amount": 200000.0
}

print(f"Incomes of the applicants: {incomes}")
print(f"Details of the applicant: {applicant}")
print(f"Income of the applicants: {applicant["income"]}")

# OPTIONAL
# credit_score can be 10.0 or 0 or None, where 0 is a value while None means nothing.

from typing import Optional

credit_score : Optional[float] = None
print(f"The CS score is: {credit_score}")

# The above can be moderly written as 
credit_score : float | None = None
print(f"The modern CS score is: {credit_score}")

credit_score = 78.0
print(f"The float CS score is: {credit_score}")

# Usage of types in Functions:
def calculate_risk_score(income: float, debt: float) -> float:
    return debt / income

def risk_decision(debt_ratio: float) -> str:
    if debt_ratio < 0.30:
        return "LOW_RISK"
    elif debt_ratio < 0.50:
        return "MEDIUM_RISK"
    else:
        return "HIGH_RISK"

ratio = calculate_risk_score(100000, 30000)
decision = risk_decision(ratio)

print(f"Risk ratio: {ratio}")
print(f"Decision: {decision}")

# list & dict in functions
def average_incomes(incomes: list[float]) -> float:
    return sum(incomes) / len(incomes)

incomes = [50000.0, 75000.0, 100000.0]
result = average_incomes(incomes)
print(result)

def calculate_debt_ratio(applicant: dict[str, float]) -> float:
    return applicant["debt"] / applicant["income"]

applicant = {
    "income": 100000.0,
    "debt": 30000.0
}

ratio = calculate_debt_ratio(applicant)
print(ratio)

# Dataclasses - will avoide uage of __init__() but can still have methods
from dataclasses import dataclass

@dataclass
class Applicant:
    income:float
    debt:float
    loan_amount:float

    def debt_ratio(self) -> float:
        return self.debt / self.income

applicant = Applicant(
    income=100000.0,
    debt=30000.0,
    loan_amount=200000.0
)
print(applicant)
print(applicant.income)
print(applicant.debt)
print(applicant.loan_amount)
print(f"Debt ratio: {applicant.debt_ratio()}")

# default values, sometimes loan amount is not sanctioned in th beginning itself so:
@dataclass
class Applicant:
    income: float
    debt: float
    loan_amount: float = 0.0

    def debt_ratio(self) -> float:
        return self.debt / self.income

applicant1 = Applicant(100000.0, 30000.0, 200000.0)
applicant2 = Applicant(150000.0, 40000.0)

print(applicant1)
print(applicant2)

# Add __post_init__() for dataclass validation, because dataclass will not validate values on its own
from dataclasses import dataclass

@dataclass
class Applicant:
    income: float
    debt: float
    loan_amount: float = 0.0

    def __post_init__(self):
        if self.income <= 0:
            raise ValueError("Income must be greater than zero")

        if self.debt < 0:
            raise ValueError("Debt cannot be negative")

        if self.loan_amount < 0:
            raise ValueError("Loan amount cannot be negative")

    def debt_ratio(self) -> float:
        return self.debt / self.income

applicant = Applicant(100000, 30000, 200000)
Applicant(0, 30000, 200000)
Applicant(100000, -30000, 200000)

# PROPERTY - will make a method as a calculated attribute
@dataclass
class Applicant:
    income: float
    debt: float
    loan_amount: float = 0.0

    def __post_init__(self):
        if self.income <= 0:
            raise ValueError("Income must be greater than zero")

        if self.debt < 0:
            raise ValueError("Debt cannot be negative")

        if self.loan_amount < 0:
            raise ValueError("Loan amount cannot be negative")
    
    @property
    def debt_ratio(self) -> float:
        return self.debt / self.income

    @property
    def loan_to_income(self) -> float:
        return self.loan_amount / self.income

applicant = Applicant(100000.0, 30000.0, 200000.0)

print(f"Debt ratio: {applicant.debt_ratio}") # instead of print(applicant.debt_ratio())
print(f"Loan to income: {applicant.loan_to_income}")

"""
Normal method
    self → specific instance
    Usually works with instance data

Class method
    cls → class
    Works with class-level information
    Can create instances

Static method
    nothing automatically
    Just a function placed inside the class
"""

# static method and class method
@dataclass
class Applicant:
    income: float
    debt: float
    loan_amount: float = 0.0

    def __post_init__(self):
        if self.income <= 0:
            raise ValueError("Income must be greater than zero")

        if self.debt < 0:
            raise ValueError("Debt cannot be negative")

        if self.loan_amount < 0:
            raise ValueError("Loan amount cannot be negative")
    
    @property
    def debt_ratio(self) -> float:
        return self.debt / self.income

    @property
    def loan_to_income(self) -> float:
        return self.loan_amount / self.income

    @staticmethod
    def is_valid_income(income: float) -> bool:
        return income > 0

    @classmethod
    def create_default(cls):
        return cls(100000.0, 30000.0, 0.0)

applicant = Applicant(100000.0, 30000.0, 200000.0)

print(Applicant.is_valid_income(100000)) #calling the static method
default_applicant = Applicant.create_default()# calling the class method
print(default_applicant)
print(applicant) # calling the instance of self method
