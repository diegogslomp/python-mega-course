from datetime import datetime


def calculate_age(year_of_birth: int, current_year: int = datetime.now().year) -> int:
    return current_year - year_of_birth
