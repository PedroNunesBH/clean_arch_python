import pytest

from domain.entities.loan_applicant import LoanApplicant


def test_loan_applicant_creation_success():
    valid_data = {
        "id": 1,
        "name": "João da Silva",
        "age": 30,
        "monthly_income": 5000.00,
        "score": 750,
    }

    applicant = LoanApplicant(**valid_data)

    assert applicant.id == valid_data["id"]
    assert applicant.name == valid_data["name"]
    assert applicant.age == valid_data["age"]
    assert applicant.monthly_income == valid_data["monthly_income"]
    assert applicant.score == valid_data["score"]


def test_create_loan_applicant_with_negative_id():
    with pytest.raises(ValueError) as exc_info:
        LoanApplicant(-1, "João da Silva", 19, 2100.00, 730)

    assert str(exc_info.value) == "ID must be a positive integer"


def test_create_loan_applicant_with_empty_name():
    with pytest.raises(ValueError) as exc_info:
        LoanApplicant(1, "", 19, 2100.00, 730)

    assert str(exc_info.value) == "Name cannot be empty or null"


def test_create_loan_applicant_with_negative_age():
    with pytest.raises(ValueError) as exc_info:
        LoanApplicant(1, "João da Silva", -19, 2100.00, 730)

    assert str(exc_info.value) == "Age cannot be negative"


def test_create_loan_applicant_with_negative_monthly_income():
    with pytest.raises(ValueError) as exc_info:
        LoanApplicant(1, "João da Silva", 19, -2100.00, 730)

    assert str(exc_info.value) == "Monthly income cannot be negative"


def test_create_loan_applicant_with_invalid_score():
    with pytest.raises(ValueError) as exc_info:
        LoanApplicant(1, "João da Silva", 19, 2100.00, 1250)

    assert str(exc_info.value) == "Score must be between 0 and 1000"
