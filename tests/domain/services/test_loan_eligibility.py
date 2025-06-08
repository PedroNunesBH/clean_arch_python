from src.domain.entities.loan_applicant import LoanApplicant
from src.domain.services.loan_eligibility_service import LoanEligibilityService


def test_loan_eligibility_with_disallowed_age():
    applicant = LoanApplicant(1, "João Paulo", 13, 2500.00, 800.00)
    is_eligible = LoanEligibilityService.is_eligible(applicant)

    assert not is_eligible


def test_loan_eligibility_with_less_than_minimun_montly_income():
    applicant = LoanApplicant(1, "João Paulo", 19, 1500.00, 890.00)
    is_eligible = LoanEligibilityService.is_eligible(applicant)

    assert not is_eligible


def test_loan_eligibility_with_low_score():
    applicant = LoanApplicant(1, "João Paulo", 22, 2500.00, 250.00)
    is_eligible = LoanEligibilityService.is_eligible(applicant)

    assert not is_eligible


def test_loan_eligiblity_with_eligible_applicant():
    applicant = LoanApplicant(1, "João Paulo", 22, 3000.00, 790.00)
    is_eligible = LoanEligibilityService.is_eligible(applicant)

    assert is_eligible


def test_maximum_value_allowed_to_applicants():
    first_applicant = LoanApplicant(1, "João Paulo", 23, 2500.00, 620)
    second_applicant = LoanApplicant(2, "Márcio da Silva", 35, 2500.00, 750)
    last_applicant = LoanApplicant(3, "Marcos Aurélio", 68, 2500.00, 890)

    first_applicant_maximum_value = LoanEligibilityService.maximum_value_allowed(
        first_applicant
    )
    second_applicant_maximum_value = LoanEligibilityService.maximum_value_allowed(
        second_applicant
    )
    last_applicant_maximum_value = LoanEligibilityService.maximum_value_allowed(
        last_applicant
    )

    assert first_applicant_maximum_value == first_applicant.monthly_income * 3
    assert second_applicant_maximum_value == second_applicant.monthly_income * 6
    assert last_applicant_maximum_value == last_applicant.monthly_income * 10
