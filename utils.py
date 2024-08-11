import re

WORD_PATTERN = '[a-zA-Z]+'


def get_words(text: str) -> list[str]:
    """
    >>> text = 'You are... awesome!'
    >>> words = get_words(text)
    >>> words
    ['you', 'are', 'awesome']
    """
    return re.findall(WORD_PATTERN, str(text).lower())