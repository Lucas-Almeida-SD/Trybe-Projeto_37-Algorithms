def validate_nums(nums):
    if not isinstance(nums, list):
        return False

    if len(nums) <= 1:
        return False

    for number in nums:
        if not isinstance(number, int) or number < 0:
            return False

    return True


def generate_numbers_dict(nums):
    numbers_dict = {}

    for number in nums:
        if number in numbers_dict:
            numbers_dict[number] += 1
        else:
            numbers_dict[number] = 1

    return numbers_dict


def generate_duplicate_numbers(numbers_dict):
    duplicate_numbers = []

    for key in numbers_dict:
        if numbers_dict[key] >= 2:
            duplicate_numbers.append(key)

    return duplicate_numbers


def find_duplicate(nums):
    if not validate_nums(nums):
        return False

    numbers_dict = generate_numbers_dict(nums)
    duplicate_numbers = generate_duplicate_numbers(numbers_dict)

    if len(duplicate_numbers) == 0 or len(duplicate_numbers) > 1:
        return False

    return duplicate_numbers[0]
