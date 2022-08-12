__all__ = (
    'seconds_to_str',
)

import time


def seconds_to_str(seconds: int) -> str:
    """
    Функция должна вернуть текстовое представление времени
    20 -> 20s
    60 -> 01m00s
    65 -> 01m05s
    3700 -> 01h01m40s
    93600 -> 01d02h00m00s
    """
    if seconds == None or seconds == 0:
        return '00s'
    else:
        seconds = int(seconds)
        d = seconds // (3600 * 24)
        h = seconds // 3600 % 24
        m = seconds % 3600 // 60
        s = seconds % 3600 % 60
        if d > 0:
            return '{:02d}d{:02d}h{:02d}m{:02d}s'.format(d, h, m, s)
        elif h > 0:
            return '{:02d}h{:02d}m{:02d}s'.format(h, m, s)
        elif m > 0:
            return '{:02d}m{:02d}s'.format(m, s)
        elif s > 0:
            return '{:02d}s'.format(s)
