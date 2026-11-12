"""Runner-up score problem: read from standard input, print one answer.

Input format:
    n
    score_1 score_2 ... score_n

Scores may appear across multiple lines; at least two distinct values exist.
"""

import sys


def second_highest_distinct(scores):
    """Find the second-highest *distinct* score, ignoring duplicates."""
    unique_scores = sorted(set(scores), reverse=True)
    return unique_scores[1]


def main():
    """Use standard input/output, as expected in coding competitions."""
    data = list(map(int, sys.stdin.read().split()))
    if not data:
        return
    n = data[0]
    scores = data[1:]
    if not 2 <= n <= 100 or len(scores) != n:
        raise ValueError("Expected n (2-100) followed by exactly n scores")
    if any(score < 0 or score > 100 for score in scores):
        raise ValueError("Scores must be between 0 and 100")
    if len(set(scores)) < 2:
        raise ValueError("At least two distinct scores are required")
    print(second_highest_distinct(scores))


if __name__ == "__main__":
    main()
