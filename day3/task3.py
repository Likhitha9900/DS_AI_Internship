# Student Grade Calculator

name = input("Enter Name: ")

marks = []
i = 1

while True:
    m = input(f"Enter Mark {i} (or 'done' to stop): ")

    if m.lower() == "done":
        break

    marks.append(int(m))
    i += 1

if marks:
    avg = sum(marks) / len(marks)

    if avg >= 90:
        grade = "A+"
    elif avg >= 80:
        grade = "A"
    elif avg >= 70:
        grade = "B"
    elif avg >= 60:
        grade = "C"
    elif avg >= 50:
        grade = "D"
    else:
        grade = "F"

    print("\nStudent Report")
    print("Name    :", name)
    print("Marks   :", marks)
    print("Average :", round(avg, 2))
    print("Grade   :", grade)
else:
    print("Marks not entered.")