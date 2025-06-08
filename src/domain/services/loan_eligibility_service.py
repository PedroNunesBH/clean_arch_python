from src.domain.entities.loan_applicant import LoanApplicant
from src.domain.services.loan_eligibility_interface import ILoanEligibilityService


class LoanEligibilityService(ILoanEligibilityService):

    @staticmethod
    def is_eligible(loan_applicant: LoanApplicant) -> bool:
        return (
            loan_applicant.age >= 18
            and loan_applicant.monthly_income >= 2000
            and loan_applicant.score >= 600
        )

    @staticmethod
    def maximum_value_allowed(loan_applicant: LoanApplicant) -> float:
        if loan_applicant.score >= 800:
            return loan_applicant.monthly_income * 10

        elif loan_applicant.score >= 700:
            return loan_applicant.monthly_income * 6

        elif loan_applicant.score >= 600:
            return loan_applicant.monthly_income * 3

        else:
            return 0.0
