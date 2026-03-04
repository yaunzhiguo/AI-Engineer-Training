def add_student(students: dict[str, int], name: str, score: int) -> None:
    students[name] = score


def get_student(students: dict[str, int], name: str):
    return students.get(name, "Student not found")


def delete_student(students: dict[str, int], name: str) -> bool:
    if name in students:
        del students[name]
        return True
    return False


def show_all_students(students: dict[str, int]) -> None:
    if not students:
        print("No students yet.")
        return

    for name, score in sorted(students.items(), key=lambda x: x[1], reverse=True):
        print(f"{name}: {score}")



def read_int(prompt: str) -> int:
    """持续读取直到用户输入一个合法整数"""
    while True:
        s = input(prompt).strip()
        try:
            return int(s)
        except ValueError:
            print("Please input an integer, e.g. 90.")


def main() -> None:
    students: dict[str, int] = {}

    while True:
        print("\n===== Student System =====")
        print("1) Add student")
        print("2) Get student")
        print("3) Delete student")
        print("4) Show all students")
        print("0) Exit")

        choice = input("Choose: ").strip()

        if choice == "1":
            name = input("name: ").strip()
            score = read_int("score: ")
            add_student(students, name, score)
            print("OK.")

        elif choice == "2":
            name = input("name: ").strip()
            result = get_student(students, name)
            print(result)

        elif choice == "3":
            name = input("name: ").strip()
            ok = delete_student(students, name)
            if ok:
                print("Deleted.")
            else:
                print("Student not found.")

        elif choice == "4": 
            show_all_students(students)

        elif choice == "0":
            print("Bye!")
            break

        else:
            print("Invalid choice. Please input 0-4.")


if __name__ == "__main__":
    main()