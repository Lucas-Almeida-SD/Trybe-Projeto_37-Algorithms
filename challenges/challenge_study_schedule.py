def validate_parameters(permanence_period, target_time):
    if type(permanence_period) is not list or len(permanence_period) == 0:
        return False
    if type(target_time) is not int:
        return False
    return True


def validate_permanence_period(permanence_period):
    try:
        for element1, element2 in permanence_period:
            if type(element1) is not int or type(element2) is not int:
                return False
    except Exception:
        return False
    return True


def study_schedule(permanence_period, target_time):
    if not validate_parameters(permanence_period, target_time):
        return None

    if not validate_permanence_period(permanence_period):
        return None

    count = 0

    for entry, exit in permanence_period:
        if entry <= target_time <= exit:
            count += 1

    return count
