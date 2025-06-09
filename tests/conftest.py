from unittest.mock import Mock

import pytest

from src.application.use_cases.loan_eligibility_use_case import (
    CheckLoanEligibilityUseCase,
)


@pytest.fixture
def mock_service():
    return Mock()


@pytest.fixture
def use_case(mock_service):
    return CheckLoanEligibilityUseCase(mock_service)
