#!/usr/bin/python3
"""lockboxes problem"""


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    opened = set(boxes[0])
    for i, box in enumerate(boxes):
        if len(box) == 0:
            if i != len(boxes) - 1:
                return False
            continue
        for key in box:
            if key not in opened:
                opened.add(key)
    return set(range(1, len(boxes))).issubset(opened)
