# Pydantic can check whether the value makes sense for:
# income: float
# This becomes particularly important when FastAPI receives data from an API request.

"""
Pydantic doesn't make API calls. FastAPI handles the API. Pydantic validates and structures the data moving through the API.
Use Pydantic whenever structured data enters, leaves, or crosses important boundaries in your system.
"""
from pydantic import BaseModel, Field

class Applicant(BaseModel):
    name: str
    income: float
    debt: float

applicant = Applicant(
    name="Sowmya",
    income=100000,
    debt=30000
)

print(applicant)

# Invalid testing  - pydantic validates on its own usign the BaseModel.
applicant1 = Applicant(
    name="Sowmya",
    income="hello",
    debt=30000
)

print(applicant1)

# gt=0 → income must be greater than 0
# ge=0 → debt must be greater than or equal to 0
"""
gt → >       greater than
ge → ≥       greater than or equal to

lt → <       lesser than
le → ≤       lesser than or equal to
"""

class Applicant(BaseModel):
    name: str
    income: float = Field(gt=0)
    debt: float = Field(ge=0)

applicant3 = Applicant(
    name="Sowmya",
    income=100000,
    debt=30000
)

print(applicant3)
