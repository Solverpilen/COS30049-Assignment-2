from datetime import date
from math import floor
from time import mktime


def foundDate(array: list, index: int, target: date, after: bool, arraylen: int) -> int | str :
    t = mktime(target.timetuple())
    if (array[index]['x'] == t):
        return index # Lucky
    elif (after == False):
        if ((index == 0) & (array[index]['x'] > t)):
            return index # year is before our range
        elif (array[index - 1]['x'] < t < array[index]['x']):
            return index - 1
        else:
            return 'above'
    else:
        if ((index == arraylen) & (array[index]['x'] < t)):
            return index # year is after our range for some reason (we should be predicting)
        elif (array[index]['x'] < t < array[index + 1]['x']):
            return index + 1
        else:
            return 'below'


def binarySearch(array: list, target: date, after=False) -> int | bool:
    arraylen = len(array) - 1
    L: int = 0 # lower bound of search
    R: int = arraylen # upper bound of search
    m: int = 0 # midpoint of L and R - the needle of the search

    while L <= R:
        m = floor((L + R) / 2)
        res = foundDate(array, m, target, after, arraylen)
        match (res):
            case 'above':
                L = m + 1
            case 'below':
                R = m - 1
            case _:
                return res
    
    return False