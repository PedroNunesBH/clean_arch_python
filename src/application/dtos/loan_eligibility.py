from dataclasses import dataclass


@dataclass
class LoanApplicationRequest:
    id: int
    name: str
    age: int
    monthly_income: float
    score: float


@dataclass
class LoanApplicationResponse:
    is_eligible: bool
    maximum_value: float
