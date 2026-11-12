"""Placement Readiness Tracker (IRP-II CSE2596).

Keeps a list of student score dictionaries, validates input and prints a report.
"""

# Each dictionary stores a name, roll number and three integer marks (0-100).
STUDENTS = [
    {"name": "Aarav", "roll_no": "24CSE001", "aptitude": 85, "verbal": 82, "coding": 90},
    {"name": "Meera", "roll_no": "24CSE002", "aptitude": 72, "verbal": 68, "coding": 65},
    {"name": "Rohan", "roll_no": "24CSE003", "aptitude": 32, "verbal": 38, "coding": 35},
    {"name": "Sara", "roll_no": "24CSE004", "aptitude": 45, "verbal": 49, "coding": 41},
    {"name": "Kabir", "roll_no": "24CSE005", "aptitude": 93, "verbal": 88, "coding": 95},
]


def read_nonempty(label):
    """Read non-blank text, preserving alphanumeric roll numbers."""
    while True:
        value = input(label).strip()
        if value:
            return value
        print("This field cannot be blank. Please try again.")


def read_score(subject):
    """Use a loop to accept only integer scores between 0 and 100."""
    while True:
        raw = input(f"Enter {subject} score (0-100): ").strip()
        try:
            score = int(raw)
        except ValueError:
            print("Invalid score: enter a whole number.")
            continue
        if 0 <= score <= 100:
            return score
        print("Invalid score: value must be from 0 to 100.")


def add_student(students):
    """Append one student created from interactive input."""
    print("\nEnter details for one additional student:")
    name = read_nonempty("Enter name: ")
    while True:
        roll_no = read_nonempty("Enter roll number: ")
        if all(student["roll_no"].lower() != roll_no.lower() for student in students):
            break
        print("That roll number already exists. Enter a unique roll number.")

    student = {"name": name, "roll_no": roll_no}
    for subject in ("aptitude", "verbal", "coding"):
        student[subject] = read_score(subject)  # Convert input text into an int.
    students.append(student)
    print(f"\nAdded {name} successfully.")


def average(student):
    """Return the average of the three subject scores."""
    return (student["aptitude"] + student["verbal"] + student["coding"]) / 3


def grade(avg):
    """Assign grades according to the prescribed thresholds."""
    if avg >= 80:
        return "A"
    if avg >= 60:
        return "B"
    if avg >= 40:
        return "C"
    return "Needs practice"


def top_scorer(students):
    """Return the student with the highest average score."""
    return max(students, key=average)


def needs_practice(students, limit=40):
    """Return students with an average strictly below the given limit."""
    return [student for student in students if average(student) < limit]


def display_results(students):
    """Print a readable table and identify students needing practice."""
    header = (f"{'Name':<12} {'Roll No':<12} {'Apt':>5} {'Verb':>5} "
              f"{'Code':>5} {'Avg':>7}  {'Grade':<15}")
    print("\n" + header)
    print("-" * len(header))
    for student in students:
        avg = average(student)
        print(f"{student['name']:<12} {student['roll_no']:<12} "
              f"{student['aptitude']:>5} {student['verbal']:>5} "
              f"{student['coding']:>5} {avg:>7.2f}  {grade(avg):<15}")

    best = top_scorer(students)
    print(f"\nTop scorer: {best['name']} ({best['roll_no']}) "
          f"with average {average(best):.2f}")

    practice_list = needs_practice(students)  # Uses the default limit of 40.
    if practice_list:
        print("Students needing extra practice (average below 40):")
        for student in practice_list:
            print(f"  - {student['name']} ({student['roll_no']}): "
                  f"{average(student):.2f}")
    else:
        print("No students need extra practice (average below 40).")


def main():
    """Build the student list and run the interactive application."""
    print("=" * 75)
    print("PLACEMENT READINESS TRACKER")
    print("=" * 75)
    students = [student.copy() for student in STUDENTS]
    add_student(students)
    print(f"\nTotal students recorded: {len(students)}")
    display_results(students)


if __name__ == "__main__":
    main()
