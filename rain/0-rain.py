#!/usr/bin/python3
"""Module for the rain function."""


def rain(walls):
    """Return the units of rainwater retained between the walls.

    Uses two pointers moving inward, tracking the tallest wall seen from
    each side. Water above a position is limited by the shorter of the two
    tallest walls around it. The ends of the list never retain water.
    """
    if not walls:
        return 0
    left, right = 0, len(walls) - 1
    left_max, right_max = walls[left], walls[right]
    total = 0
    while left < right:
        if walls[left] <= walls[right]:
            left += 1
            if walls[left] > left_max:
                left_max = walls[left]
            else:
                total += left_max - walls[left]
        else:
            right -= 1
            if walls[right] > right_max:
                right_max = walls[right]
            else:
                total += right_max - walls[right]
    return total
