FREEZING_POINT = 0
BOILING_POINT = 100

def state_of_water(temperature: float) -> str:
    if temperature <= FREEZING_POINT:
        return "Solid"
    elif temperature >= BOILING_POINT:
        return "Gas"
    else:
        return "Liquid"
