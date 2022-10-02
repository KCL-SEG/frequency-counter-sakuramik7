"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    items = [str(value) for value in items]
    lastv = len(items)
    while 0 != lastv:
        x = 0
        temp = items[0]
        items.pop(0)
        lastv = lastv -1
        count = 1
        while x != lastv:
            if (temp == items[x]):
                count = count + 1
                items.pop(x)
                lastv = lastv -1
            else:
                x = x + 1

        frequencies.update({temp:count})
    return frequencies
