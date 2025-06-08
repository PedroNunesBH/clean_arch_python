from abc import ABC, abstractmethod

from src.domain.entities.loan_applicant import LoanApplicant


class ILoanEligibilityService(ABC):
    @staticmethod
    @abstractmethod
    def is_eligible(loan_applicant: LoanApplicant) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def maximum_value_allowed(loan_applicant: LoanApplicant) -> float:
        pass
