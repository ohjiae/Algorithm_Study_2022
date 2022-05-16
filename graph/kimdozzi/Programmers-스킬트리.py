import sys
from collections import deque


def solution(skill, skill_trees):
    count = 0
    for trees in skill_trees:
        queue = deque(skill)
        for tree in trees:
            if tree in queue and tree != queue.popleft():
                break
        else:
            count += 1
    return count


if __name__ == "__main__":
    skill = "ABC"
    skill_trees = ["OPQ"]

    print(solution(skill, skill_trees))
