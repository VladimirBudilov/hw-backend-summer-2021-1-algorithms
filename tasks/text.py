from typing import Optional

__all__ = (
    'find_shortest_longest_word',
)


def find_shortest_longest_word(text: str) -> tuple[Optional[str], Optional[str]]:
    """
    В переданном тексте вернуть слово имеющее наименьшую и наибольшую длину.
    Если такого слова нет - вернуть None
    """
    text = text.split()
    if len(text) > 1:
        mn = min(text, key=len)
        mx = max(text, key=len)
    else:
        mn = mx = None
    return mn, mx
