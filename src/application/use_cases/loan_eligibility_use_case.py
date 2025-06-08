from src.application.dtos.loan_eligibility import (
    LoanApplicationRequest,
    LoanApplicationResponse,
)
from src.domain.entities.loan_applicant import LoanApplicant
from src.domain.services.loan_eligibility_interface import ILoanEligibilityService


class CheckLoanEligibilityUseCase:
    def __init__(self, loan_eligibility_service: ILoanEligibilityService) -> None:
        self._loan_eligibility_service = loan_eligibility_service

    def execute(self, request: LoanApplicationRequest) -> LoanApplicationResponse:
        try:
            applicant = LoanApplicant(
                id=request.id,
                name=request.name,
                age=request.age,
                monthly_income=request.monthly_income,
                score=request.score,
            )

            is_eligible = self._loan_eligibility_service.is_eligible(applicant)

            if is_eligible:
                max_value = self._loan_eligibility_service.maximum_value_allowed(
                    applicant
                )
            else:
                max_value = 0.0

            return LoanApplicationResponse(
                is_eligible=is_eligible, maximum_value=max_value
            )

        except ValueError as exc:
            raise ValueError(f"Invalid applicant data: {str(exc)}")
