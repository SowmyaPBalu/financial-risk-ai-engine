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

# MINI EXERCISE
@dataclass
class LoanApplicant():
    name:str
    income:float
    debt:float
    loan_amount:float

    loan_type = "General"

# 1. Validation using __post_init__
    def __post_init__(self):
        if self.income <0.0:
            raise ValueError("Income must be greater than 0")
        if self.debt <0.0:
            raise ValueError("Debt cannot be negative")
        if self.loan_amount <0.0:
            raise ValueError("Loan amoount cannot be negative")

# Property 
    @property
    def ratio(self) -> float: 
        return self.debt / self.income

# Static method
    @staticmethod
    def is_valid_income(income) -> bool:
        return income > 0

# class method
    @classmethod
    def create_default(cls):
        return cls("Shiksha",100000.0, 30000.0, 0.0)

applicant = LoanApplicant("Shiksha",100000.0,30000.0,200000.0)
applicant1 = LoanApplicant("Shiksha",-1.0,30000.0,200000.0)
applicant2 = LoanApplicant("Shiksha",100000.0,-9.0,200000.0)
applicant3 = LoanApplicant("Shiksha",100000.0,30000.0,-798.0)
LoanApplicant.is_valid_income(189879)
default_applicant = LoanApplicant.create_default()# calling the class method
print(default_applicant)
print(LoanApplicant.ratio)

# 28/SEP/2026
# DECORATORS
def calculate_risk():
    return "LOW_RISK"

my_function = calculate_risk
print(my_function())

# Passing a function into a function
def calculate_risk():
    return "LOW_RISK"

def execute_function(func):
    return func()

result = execute_function(calculate_risk)
print(result)

# skeleton for decorator
def calculate_risk():
    return "LOW_RISK"

def log_execution(func):

    def wrapper():
        print("Function started")
        result = func()
        print("Function completed")
        return result
    return wrapper

calculate_risk = log_execution(calculate_risk) #decorator piece
result = calculate_risk()
print(result)

# ACTUAL Decorator
def log_execution(func):

    def wrapper():
        print("Function started")
        result = func()
        print("Function completed")
        return result
    return wrapper

@log_execution #decorator will do calculate_risk = log_execution(calculate_risk)
def calculate_risk():
    return "LOW_RISK"

result = calculate_risk()
print(result)

# args &kwargs
def log_execution(func):

    def wrapper(*args):
        print("Function started")
        result = func(*args)
        print("Function completed")
        return result
    return wrapper

@log_execution
def calculate_risk_score(income, debt):
    return debt / income

result = calculate_risk_score(100000, 30000)
print(result)

# positional arguments -> tuple
def test(*args):
    print(args)
test(100000,30000)

# Key word arguments -> dictionary
def test(**kwargs):
    print(kwargs)
test(income=100000, debt=30000)

# Usage of args & kwargs in decorators
def log_execution(func):

    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper

@log_execution
def calculate_risk_score(income, debt):
    return debt / income

calculate_risk_score(100000, 30000)
calculate_risk_score(income=100000, debt=30000)

# @wraps
from functools import wraps

def log_execution(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result

    return wrapper

@log_execution
def calculate_risk_score(income, debt):
    return debt / income

print(calculate_risk_score.__name__)
help(calculate_risk_score)

# Good ex
def a_decorator(func):
    def wrapper(*args, **kwargs):
        """A wrapper function"""
        # Extend some capabilities of func
        func()
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@a_decorator
def first_function():
    """This is docstring for first function"""
    print("first function")

@a_decorator
def second_function(a):
    """This is docstring for second function"""
    print("second function")

print(first_function.__name__)
print(first_function.__doc__)
print(second_function.__name__)
print(second_function.__doc__)

# GENERATORS [29/SEP/2026]
"""
A generator in Python is a special type of iterator that produces values 
one at a time, on demand, using yield, instead of creating and storing all 
the values in memory at once.
"""
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()
print(numbers)
print(next(numbers))
print(next(numbers))
print(next(numbers))

# FOR LOOP
def get_numbers():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5

numbers = get_numbers()
for number in numbers:
    print(number)

# FOR EACH APPLICANT
def get_applicants():
    yield {"income": 100000, "debt": 30000}
    yield {"income": 80000, "debt": 40000}
    yield {"income": 150000, "debt": 20000}


for applicant in get_applicants():
    print(applicant)

# FOR EACH DEBT RATIO
def get_applicants():
    yield {"income": 100000, "debt": 30000}
    yield {"income": 80000, "debt": 40000}
    yield {"income": 150000, "debt": 20000}
    yield {"income": 1299829, "debt": 278363}
    yield {"income": 245613675, "debt": 267253}

for i, applicant in enumerate(get_applicants(), start=1):
    ratio = applicant["debt"] / applicant["income"]
    print(f"The debt ratio for applicant {i}: {ratio}")

# Generator vs List
# list
def get_numbers():
    return [i for i in range(1, 1000001)]
# get_numbers()

# Generator
def get_numbers():
    for i in range(1,1000001):
        yield i

numbers = get_numbers()

for number in numbers:
    if number == 999:
        print(number)
        break

# mini exercise
def get_applicants():
    yield {"income": 100000, "debt": 30000}
    yield {"income": 80000, "debt": 40000}
    yield {"income": 150000, "debt": 20000}

data = get_applicants()

for i, applicant in enumerate(data, start=1):
    debt_ratio = applicant["debt"]/applicant["income"]
    print(f"Applicant {i}: debt ratio = {debt_ratio}")

# 03/OCT/2026
# Context managers - with
"""
Context Manager — definition

A context manager in Python is an object that manages the setup 
and cleanup of a resource or operation automatically, using the with 
statement.

-Database connections
-Network connections
-Locks
-Transactions
-Temporary resources
"""
with open("sample.txt", "r") as file:
    data = file.read()

print(data)

# A context manager follows two special methods:
#  __enter__() & _exit__()
with open("sample.txt", "r") as file:
    data = file.read()
    print(data)
    raise ValueError("Something went wrong")

"""
exc_type - what type of error
exc_value - error message
traceback - Where did it happen
"""
class MyContext:
    def __enter__(self):
        print("Entering context")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Exiting context")

# with MyContext():
#     print("Inside context")
with MyContext():
    print("Inside context")
    raise ValueError("Test error")

# LOGGING
import logging

# "Show INFO-level messages and anything more serious."
logging.basicConfig(level=logging.INFO)
# "Record an informational message."
logging.info("Risk calculation started")

import logging
logging.basicConfig(level=logging.DEBUG,
                    filename="risk_engine.log",
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
                    )
logger = logging.getLogger("risk_engine")

logging.debug("Debug message")
logging.info("Risk calculation started")
logging.warning("High debt ratio detected")
logging.error("Risk calculation failed")
logging.critical("Risk engine unavailable")

logger.debug("Debug message")
logger.info("Risk calculation started")
logger.warning("High debt ratio detected")
logger.error("Risk calculation failed")
logger.critical("Risk engine unavailable")

def calculate_risk_score(income: float, debt: float) -> float:
    logger.info("Risk calculation started")

    if income <= 0:
        logger.error("Invalid income: income must be greater than zero")
        raise ValueError("Income must be greater than zero")

    if debt < 0:
        logger.error("Invalid debt: debt cannot be negative")
        raise ValueError("Debt cannot be negative")

    debt_ratio = debt / income

    logger.debug(f"Calculated debt ratio: {debt_ratio}")

    logger.info("Risk calculation completed")

    return debt_ratio

result = calculate_risk_score(100000, 30000)
print(f"Risk score: {result}")

try:
    result = calculate_risk_score(0, 30000)
    print(f"Risk score: {result}")
except ValueError:
    logger.exception("Risk calculation failed")

