#!/usr/bin/env python3
"""
0-making_change
"""


def makeChange(coins: [int], total: int) -> int:
    """
    Given a pile of coins of different values, determine
    the fewest number of coins needed to meet a given amount total.
    """

    if total <= 0:
        return 0

    coins.sort(reverse=True)
    change = 0
    for coin in coins:
        temp = total // coin
        change += temp
        total -= (temp * coin)
    if total != 0:
        return -1
    return change
