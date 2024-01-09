#!/usr/bin/python3
"""
Interview question: Unlock the boxes
"""


def canUnlockAll(boxes):
    """
    Return true if all the boxes can be unlocked
    Else false

    Assumption: First box is already opened

    -----------------------------------------------------------
    Pseudocode:
    Create a list of already opened boxes
    Create another list of boxes (subset of opened boxes) that \
            have already been visited
    Create another list of keys available

    Navigate from the first box which is already opened to the next

    Use keys in the first box to open all the boxes they can open
    Since any key number identifies the box it can open.

    Go through each opened yet unvisited box.
    Carry the keys and open all the boxes they can open.

    Mark the opened boxes. Mark each visited box - \
            meaning you have collected the key there.
    """

    if not (isinstance(boxes, list) or isinstance(boxes, set)):
        # Check against invalid boxes
        return False

    n = len(boxes)
    visited = [False] * n
    keys = boxes[0]

    # Mark the first box as visited
    visited[0] = True

    while keys:
        key = keys.pop()

        try:
            # Check if the corresponding box is already unlocked
            if visited[key]:
                continue

        # Mark the box as unlocked and add its keys to the list
            visited[key] = True     # Error here
            keys.extend(boxes[key])
        except IndexError:
            # A key for an uknown box present
            # Don't attempt opening such box
            pass

    # True if all boxes visited is set to True
    return all(visited)
