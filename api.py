from fastapi import FastAPI
from pydantic import BaseModel, Field

"""
Is Swagger required? No.
API works perfectly without Swagger.
FastAPI simply gives you the documentation/testing UI automatically, which is extremely convenient during development.
"""
# python -m uvicorn api:app --reload

app = FastAPI()

class Applicant(BaseModel):
    name: str
    income: float = Field(gt=0)
    debt: float = Field(ge=0)

# When someone sends a POST request to /risk, run this function.
@app.post("/risk")
def calculate_risk(applicant: Applicant):
    debt_ratio = applicant.debt / applicant.income

    return {
        "name": applicant.name,
        "debt_ratio": debt_ratio
    }
