# Placement Readiness Tracker

A Python command-line tool for recording student practice scores and identifying students who need further preparation. Developed for IRP-II (CSE2596), Assessment 4.

## Requirements

- Python 3.9 or later
- No external libraries required

## Files

- `placement_tracker.py` — interactive placement readiness tracker (Tasks 1 and 2)
- `runner_up.py` — competitive-programming runner-up score solution (Task 3)
- `tests/test_programs.py` — automated unit tests

## Running

```bash
python placement_tracker.py
python runner_up.py
```

Enter scores only as integers from 0 to 100. The program prompts again for invalid scores. The runner-up program reads `n` on the first line and `n` integer scores on the next line(s), without interactive prompts.

## Git history

A feature branch named `feature-grades` was merged into `main`, and the repository contains at least five meaningful commits. Use `git log --oneline --graph --all` to review the history.
