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


def main():
    """Build the student list and run the interactive application."""
    print("=" * 75)
    print("PLACEMENT READINESS TRACKER")
    print("=" * 75)
    students = [student.copy() for student in STUDENTS]
    add_student(students)
    print(f"\nTotal students recorded: {len(students)}")


if __name__ == "__main__":
    main()
