"""Automated verification for tasks 1-3 using only the Python standard library."""

import subprocess
import sys
import unittest
from pathlib import Path

from placement_tracker import (
    STUDENTS, average, grade, needs_practice, top_scorer,
)
from runner_up import second_highest_distinct

ROOT = Path(__file__).resolve().parents[1]


class TrackerTests(unittest.TestCase):
    def test_five_records_and_average(self):
        self.assertGreaterEqual(len(STUDENTS), 5)
        self.assertAlmostEqual(average(STUDENTS[0]), (85 + 82 + 90) / 3)

    def test_grade_thresholds(self):
        for score, expected in ((80, "A"), (60, "B"), (40, "C"),
                                (39.99, "Needs practice")):
            with self.subTest(score=score):
                self.assertEqual(grade(score), expected)

    def test_top_scorer(self):
        self.assertEqual(top_scorer(STUDENTS)["name"], "Kabir")

    def test_default_practice_threshold(self):
        self.assertEqual([s["name"] for s in needs_practice(STUDENTS)], ["Rohan"])


class RunnerUpTests(unittest.TestCase):
    def test_three_distinct_cases(self):
        cases = [
            ([70, 85, 85, 60, 90], 85),
            ([90, 90, 75, 60], 75),
            ([40, 100], 40),
            ([40, 40, 40, 30, 50, 50], 40),
        ]
        for values, expected in cases:
            with self.subTest(values=values):
                self.assertEqual(second_highest_distinct(values), expected)
                program_input = f"{len(values)}\n{' '.join(map(str, values))}\n"
                completed = subprocess.run(
                    [sys.executable, str(ROOT / "runner_up.py")],
                    input=program_input,
                    capture_output=True,
                    text=True,
                    check=True,
                )
                self.assertEqual(completed.stdout.strip(), str(expected))


if __name__ == "__main__":
    unittest.main()
