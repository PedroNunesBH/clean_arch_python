import pytest

from src.application.dtos.loan_eligibility import LoanApplicationRequest
from tests.conftest import mock_service, use_case


def test_when_applicant_is_eligible(mock_service, use_case):
    request = LoanApplicationRequest(
        id=1, name="João Brasil", age=24, monthly_income=3500.00, score=890
    )
    mock_service.is_eligible.return_value = True
    mock_service.maximum_value_allowed.return_value = request.monthly_income * 10

    response = use_case.execute(request)

    assert response.is_eligible is True
    assert response.maximum_value == 35000.00
    mock_service.is_eligible.assert_called_once()
    mock_service.maximum_value_allowed.assert_called_once()


def test_when_applicant_is_not_eligible(mock_service, use_case):
    request = LoanApplicationRequest(
        id=1, name="João Silva", age=17, monthly_income=0.0, score=230
    )

    mock_service.is_eligible.return_value = False

    response = use_case.execute(request)

    assert response.is_eligible is False
    assert response.maximum_value == 0.0
    mock_service.is_eligible.assert_called_once()


def test_execute_with_invalid_data_raises_value_error(mock_service, use_case):
    request = LoanApplicationRequest(
        id="125",
        name="Invalid User",
        age=-1,
        monthly_income=4000.0,
        score=600,
    )

    with pytest.raises(ValueError, match="Invalid applicant data:"):
        use_case.execute(request)
