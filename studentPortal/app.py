from portal import StudentPortal

def main():
    portal = StudentPortal()

    print("=== STUDENT PORTAL ===")
    username = input("Username: ")
    password = input("Password: ")

    student_id = portal.login(username, password)
    if not student_id:
        print("Login failed")
        return

    print("Login success:", student_id)

    print("1. Update personal info")
    print("2. Register course")
    print("3. Cancel course")
    print("4. View grades")
    print("5. View assigned courses")
    print("6. View student list")
    
    choice = input("Choose: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        email = input("Email: ")
        portal.update_personal_info(student_id, name, phone, email)
        print("Updated")

    elif choice == "2":
        cid = input("Course ID: ")
        portal.register_course(student_id, cid)
        print("Registered")

    elif choice == "3":
        cid = input("Course ID: ")
        portal.cancel_course(student_id, cid)
        print("Canceled")

    elif choice == "4":
        print(portal.view_grades(student_id))

    elif choice == "5":
        print(portal.view_assigned_courses(student_id))

    elif choice == "6":
        students = portal.view_student_list()
        if not students:
            print("No students found")
        else:
            for s in students:
                print(f"{s['student_id']} | {s['name']} | {s['phone']} | {s['email']}")

if __name__ == "__main__":
    main()
