__all__ = (
    'is_prime',
)


def is_prime(number: int) -> bool:
    """
    Функция должна вернуть True если число является простым, иначе - False
    """
    return False if number == 1 or number == 0 else all([bool(number % x) for x in range(2, number)])
