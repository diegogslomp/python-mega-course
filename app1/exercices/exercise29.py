from datetime import datetime


def calculate_age(
    year_of_birth: int, current_year: int = datetime.now().year
) -> int | str:
    years_old = current_year - year_of_birth
    if years_old >= 120:
        return "You're old af"
    return years_old


year_of_birth = int(input("What is your year of birth? "))

print(calculate_age(year_of_birth))
