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

## Example run

Start `placement_tracker.py` and enter:

```text
Enter name: Arya
Enter roll number: 24CSE006
Enter aptitude score (0-100): 105
Invalid score: value must be from 0 to 100.
Enter aptitude score (0-100): 88
Enter verbal score (0-100): 74
Enter coding score (0-100): 91
```

The result table includes six students, with Kabir as top scorer (average 92.00). Rohan is flagged for extra practice (average 35.00).

Example of the main program's result output:

```text
Total students recorded: 6

Name         Roll No        Apt  Verb  Code     Avg  Grade
--------------------------------------------------------------------
Aarav        24CSE001        85    82    90   85.67  A
Meera        24CSE002        72    68    65   68.33  B
Rohan        24CSE003        32    38    35   35.00  Needs practice
Sara         24CSE004        45    49    41   45.00  C
Kabir        24CSE005        93    88    95   92.00  A
Arya         24CSE006        88    74    91   84.33  A

Top scorer: Kabir (24CSE005) with average 92.00
Students needing extra practice (average below 40):
  - Rohan (24CSE003): 35.00
```

Runner-up sample:

```text
Input:
5
70 85 85 60 90

Output:
85
```

## Test commands

```bash
python -m unittest discover -s tests -v
printf '5\n70 85 85 60 90\n' | python runner_up.py
```

## Publish your own GitHub repository

1. Create a new empty repository on GitHub (do not initialize with a README).
2. From this project folder, use `git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git`.
3. Use `git push -u origin main` and `git push origin feature-grades`.
4. Replace the placeholder repository address in the Word submission report with your real URL.
5. Take a screenshot of `git log --oneline` from your own terminal if your teacher requires a personal run.

**Academic integrity:** An AI assistant was used to help draft and test the code and prepare the documentation. Review and understand every line before submission.
