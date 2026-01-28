from pathlib import Path
from storage import Storage
from portal import StudentPortal, AuthError, NotFoundError, ValidationError

def main():
    base = Path(__file__).parent / "data"
    portal = StudentPortal(Storage(base))
    current_student_id = None

    while True:
        print("\n===== STUDENT PORTAL =====")
        print("1. Login")
        print("2. Update personal information")
        print("3. Register for courses")
        print("4. Cancel course registration")
        print("5. View grades")
        print("6. View assigned courses")
        print("7. View student list")
        print("0. Exit")

        choice = input("Choose: ").strip()

        try:
            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                current_student_id = portal.login(username, password)
                print("Login success! Student ID:", current_student_id)

            elif choice == "2":
                if not current_student_id:
                    print("Please login first.")
                    continue
                full_name = input("Full name: ").strip()
                dob = input("DOB (DD/MM/YYYY): ").strip()
                gender = input("Gender: ").strip()
                phone = input("Phone: ").strip()
                email = input("Email: ").strip()
                address = input("Address: ").strip()
                portal.update_personal_info(current_student_id, full_name, dob, gender, phone, email, address)
                print("Updated successfully!")

            elif choice == "3":
                if not current_student_id:
                    print("Please login first.")
                    continue
                course_id = input("Course ID: ").strip()
                portal.register_course(current_student_id, course_id)
                print("Registered successfully!")

            elif choice == "4":
                if not current_student_id:
                    print("Please login first.")
                    continue
                course_id = input("Course ID: ").strip()
                portal.cancel_registration(current_student_id, course_id)
                print("Canceled successfully!")

            elif choice == "5":
                if not current_student_id:
                    print("Please login first.")
                    continue
                grades = portal.view_grades(current_student_id)
                if not grades:
                    print("No grades found.")
                else:
                    print("Grades:")
                    for cid, score in grades:
                        print(f"- {cid}: {score}")

            elif choice == "6":
                if not current_student_id:
                    print("Please login first.")
                    continue
                courses = portal.view_assigned_courses(current_student_id)
                print("Assigned/Registered courses:", courses if courses else "None")

            elif choice == "7":
                students = portal.list_students()
                if not students:
                    print("No students.")
                else:
                    print("Student list:")
                    for s in students:
                        print(" - " + ", ".join(s))

            elif choice == "0":
                break
            else:
                print("Invalid choice!")

        except (AuthError, NotFoundError, ValidationError) as e:
            print("ERROR:", e)

if __name__ == "__main__":
    main()
