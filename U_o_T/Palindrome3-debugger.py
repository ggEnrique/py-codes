# Palindrome3
import doctest

word1 = "h"
word2 = "he"
word3 = "heh"
word4 = "heeh"


def p1(s):
    """(str) -> boolean

    Return whether a string is a palindrome or not


    >>> p1("h")
    True
    >>> p1("he")
    False
    >>> p1("heh")
    True
    >>> p1("heeh")
    True
    """
    for i in range(len(s) // 2 + 1):
        if s[i] != s[len(s) - i - 1]:
            return False

    return True


doctest.testmod()
