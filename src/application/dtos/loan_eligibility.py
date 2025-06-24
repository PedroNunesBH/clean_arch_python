from pydantic import BaseModel


class LoanApplicationRequest(BaseModel):
    id: int
    name: str
    age: int
    monthly_income: float
    score: float


class LoanApplicationResponse(BaseModel):
    is_eligible: bool
    maximum_value: float
