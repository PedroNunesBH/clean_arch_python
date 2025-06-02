class LoanApplicant:
    """
    Entity representing a user requesting a loan.
    """

    def __init__(
        self, id: int, name: str, age: int, monthly_income: float, score: float
    ) -> None:
        self.id = id
        self.name = name
        self.age = age
        self.monthly_income = monthly_income
        self.score = score
        self._validate_data()

    def _validate_data(self) -> None:
        """
        Validate basic entity data.
        """
        if not isinstance(self.id, int) or self.id <= 0:
            raise ValueError("ID must be a positive integer")

        if not isinstance(self.name, str) or not self.name.strip():
            raise ValueError("Name cannot be empty or null")

        if not isinstance(self.age, int) or self.age < 0:
            raise ValueError("Age cannot be negative")

        if not isinstance(self.monthly_income, (int, float)) or self.monthly_income < 0:
            raise ValueError("Monthly income cannot be negative")

        if not isinstance(self.score, (int, float)) or not (0 <= self.score <= 1000):
            raise ValueError("Score must be between 0 and 1000")
