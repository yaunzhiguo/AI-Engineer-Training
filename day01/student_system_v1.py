# student_system_v1.py
# Author: 9527
# Date: 2026-03-03
# Desc: CLI student score management system (V1)

students = {
    "ZhangSan": 90,
    "LiSi": 85,
}

def input_name() -> str:
    name = input("Enter name:").strip()
    if not name:
        print("Name cannot be empty.")
        return " "
    return name

def input_score() -> int | None:
    s = input("Enter score(0-100):").strip()
    try:
        score = int(s)
    except ValueError:
         print("Score must be an integer.")
         return None
    if score < 0 or score > 100:
        print("Score must be in [0, 100].")
        return None
    return score

def add_student():
    name = input_name()
    if not name:
        return
    if name in students:
        print("Student already exists.")
        return
    score = input_score()
    if score is None:
        return
    students[name] = score
    print("Added:", name, score)

def delete_student():
    name = input_name()
    if not name:
        return
    if name not in students:
        print("Not found.")
        return
    del students[name]
    print("Deleted:", name)

def query_student():
    name = input_name()
    if not name:
        return
    if name not in students:
        print("Not found.")
        return
    print(f"{name}: {students[name]}")

def update_student():
    name = input_name()
    if not name:
        return
    if name not in students:
        print("Not found.")
        return
    score = input_score()
    if score is None:
        return
    students[name] = score
    print("Updated:", name, score)

def list_all():
    if not students:
        print("(empty)")
        return
    print("\n--- All Students ---")
    for name, score in sorted(students.items(), key=lambda x: x[0].lower()):
        print(f"{name:<12} {score}")
    print("--------------------\n")

def menu():
    print("1) add")
    print("2) delete")
    print("3) query")
    print("4) update")
    print("5) list_all")
    print("6) exit")

def main():
    while True:
        menu()
        choice = input("Choose:").strip()
        if choice == "1":
            add_student()
        elif choice == "2":
            delete_student()
        elif choice == "3":
            query_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            list_all()
        elif choice == "6":
            print("Bye.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()