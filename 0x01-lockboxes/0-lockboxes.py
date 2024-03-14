#!/usr/bin/python3
"""lockboxes problem"""


opened = set()


def canUnlockAll(boxes):
    """check if all boxes can be opened"""
    boxes_len = set(range(1, len(boxes)))
    for i, box in enumerate(boxes):
        if len(box) == 0 and not i == len(boxes) - 1:
            return False
        for key in box:
            if key not in opened:
                opened.add(key)
    if boxes_len.issubset(opened):
        return True
    return False
