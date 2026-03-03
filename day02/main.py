from day02.service import StudentService
from day02.utils import input_non_empty, input_score

def menu():
    print("1) add")
    print("2) delete")
    print("3) query")
    print("4) update")
    print("5) list_all")
    print("6) exit")

def main():
    svc = StudentService()

    while True:
        menu()
        choice = input("Choose: ").strip()

        if choice == "1":
            name = input_non_empty("Enter name: ")
            if not name:
                continue
            score = input_score()
            if score is None:
                continue
            ok = svc.add(name, score)
            print("Added." if ok else "Student already exists.")

        elif choice == "2":
            name = input_non_empty("Enter name: ")
            if not name:
                continue
            ok = svc.delete(name)
            print("Deleted." if ok else "Not found.")

        elif choice == "3":
            name = input_non_empty("Enter name: ")
            if not name:
                continue
            score = svc.query(name)
            print(f"{name}: {score}" if score is not None else "Not found.")

        elif choice == "4":
            name = input_non_empty("Enter name: ")
            if not name:
                continue
            score = input_score()
            if score is None:
                continue
            ok = svc.update(name, score)
            print("Updated." if ok else "Not found.")

        elif choice == "5":
            items = svc.list_all()
            if not items:
                print("(empty)")
            else:
                print("\n--- All Students ---")
                for n, s in items:
                    print(f"{n:<12} {s}")
                print("--------------------\n")

        elif choice == "6":
            print("Bye.")
            svc.save()  
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
