from fastapi import APIRouter, HTTPException

from src.application.dtos.loan_eligibility import (
    LoanApplicationRequest,
    LoanApplicationResponse,
)
from src.application.use_cases.loan_eligibility_use_case import (
    CheckLoanEligibilityUseCase,
)
from src.domain.services.loan_eligibility_service import LoanEligibilityService

loan_router = APIRouter(prefix="/api/loan", tags=["loan"])


@loan_router.post("/eligibility")
async def check_loan_eligibility(
    request: LoanApplicationRequest,
) -> LoanApplicationResponse:
    try:
        service = LoanEligibilityService()
        use_case = CheckLoanEligibilityUseCase(service)
        return use_case.execute(request)
    except ValueError as e:
        raise HTTPException(status_code=400, detail="Bad request.")
    except Exception as e:
        raise HTTPException(status_code=500, detail="Internal Server Error")
