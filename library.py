FINE_PER_DAY = 5


def calculate_fine(late_days):
    if late_days < 0:
        raise ValueError("Late days cannot be negative")

    return late_days * FINE_PER_DAY