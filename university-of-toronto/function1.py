import doctest
from pydoc import doc


def collect_vowels(s):
    ''' (str) -> str
    Return the vowels from s

    >>> collect_vowels('Happy Anniversary')
    'aAiea'
    >>> collect_vowels('xyz')
    ''
    '''
    vowels = ""
    for char in s:
        if char in "aeiouAEIOU":
            vowels += char
    return vowels

def count_vowels(s):
    ''' (str) -> str
    Return the vowels from s

    >>> count_vowels('Happy Anniversary')
    5
    >>> count_vowels('xyz')
    0
    '''
    num_vowels = 0
    for char in s:
        if char in "aeiouAEIOU":
            num_vowels += 1
    return num_vowels

import doctest
doctest.testmod()