from repository import StudentRepository
from student_manager import StudentManager
from models import ValidationError


def main():
    repo = StudentRepository()
    manager = StudentManager(repo)

    while True:
        print("\n=== STUDENT MANAGEMENT ===")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. List students")
        print("0. Exit")

        choice = input("Choose: ")

        try:
            if choice == "1":
                manager.add_student(
                    student_id=input("ID: "),
                    full_name=input("Full name: "),
                   dob=input("DOB (DD/MM/YYYY): "),
                    gender=input("Gender: "),
                    phone=input("Phone: "),
                    email=input("Email: "),
                    address=input("Address: "),
                )
                print("Added successfully!")

            elif choice == "2":
                sid = input("Student ID: ")
                manager.update_student(
                    sid,
                    full_name=input("New name (blank to skip): "),
                    phone=input("New phone (blank to skip): "),
                    email=input("New email (blank to skip): "),
                )
                print("Updated successfully!")

            elif choice == "3":
                manager.delete_student(input("Student ID: "))
                print("Deleted!")

            elif choice == "4":
                for s in manager.list_students():
                    print(s)

            elif choice == "0":
                break

        except ValidationError as e:
            print("ERROR:", e)


if __name__ == "__main__":
    main()
