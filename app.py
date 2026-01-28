# ================= DATA =================
accounts = []
students = []
lecturers = []
courses = []
assignments = []
grades = []

current_user = None

# ================= ACCOUNT =================
def create_account():
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (admin/lecturer/student): ")
    accounts.append({"u": username, "p": password, "r": role})
    print("Account created successfully")

def login():
    global current_user
    username = input("Username: ")
    password = input("Password: ")
    for acc in accounts:
        if acc["u"] == username and acc["p"] == password:
            current_user = acc
            print("Login successful")
            return
    print("Invalid username or password")

def logout():
    global current_user
    current_user = None
    print("Logged out")

def check_role():
    if current_user:
        print("Role:", current_user["r"])
    else:
        print("Not logged in")

def view_accounts():
    for acc in accounts:
        print(acc)

def delete_account():
    username = input("Username to delete: ")
    global accounts
    accounts = [acc for acc in accounts if acc["u"] != username]
    print("Account deleted")

def account_menu():
    while True:
        print("\n===== ACCOUNT MANAGEMENT =====")
        print("1. Create account")
        print("2. Login")
        print("3. Logout")
        print("4. Check role")
        print("5. View accounts")
        print("6. Delete account")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            create_account()
        elif choice == "2":
            login()
        elif choice == "3":
            logout()
        elif choice == "4":
            check_role()
        elif choice == "5":
            view_accounts()
        elif choice == "6":
            delete_account()
        elif choice == "0":
            break

# ================= STUDENT =================
def add_student():
    students.append({
        "id": input("Student ID: "),
        "name": input("Student name: ")
    })
    print("Student added")

def update_student():
    sid = input("Student ID to update: ")
    for s in students:
        if s["id"] == sid:
            s["name"] = input("New name: ")
            print("Student updated")
            return
    print("Student not found")

def delete_student():
    sid = input("Student ID to delete: ")
    global students
    students = [s for s in students if s["id"] != sid]
    print("Student deleted")

def view_students():
    for s in students:
        print(s)

def student_menu():
    while True:
        print("\n===== STUDENT MANAGEMENT =====")
        print("1. Add student")
        print("2. Update student")
        print("3. Delete student")
        print("4. View students")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            update_student()
        elif choice == "3":
            delete_student()
        elif choice == "4":
            view_students()
        elif choice == "0":
            break

# ================= LECTURER =================
def add_lecturer():
    lecturers.append({
        "id": input("Lecturer ID: "),
        "name": input("Lecturer name: ")
    })
    print("Lecturer added")

def delete_lecturer():
    lid = input("Lecturer ID to delete: ")
    global lecturers
    lecturers = [l for l in lecturers if l["id"] != lid]
    print("Lecturer deleted")

def update_lecturer():
    lid = input("Lecturer ID to update: ")
    for l in lecturers:
        if l["id"] == lid:
            l["name"] = input("New name: ")
            print("Lecturer updated")
            return
    print("Lecturer not found")

def assign_course():
    assignments.append({
        "lid": input("Lecturer ID: "),
        "cid": input("Course ID: ")
    })
    print("Course assigned")

def view_assigned_courses():
    lid = input("Lecturer ID: ")
    for a in assignments:
        if a["lid"] == lid:
            print("Course:", a["cid"])

def enter_grade():
    grades.append({
        "sid": input("Student ID: "),
        "cid": input("Course ID: "),
        "grade": input("Grade: ")
    })
    print("Grade entered")

def lecturer_menu():
    while True:
        print("\n===== LECTURER MANAGEMENT =====")
        print("1. Add lecturer")
        print("2. Delete lecturer")
        print("3. Update lecturer")
        print("4. Assign course")
        print("5. View assigned courses")
        print("6. View students")
        print("7. Enter grade")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_lecturer()
        elif choice == "2":
            delete_lecturer()
        elif choice == "3":
            update_lecturer()
        elif choice == "4":
            assign_course()
        elif choice == "5":
            view_assigned_courses()
        elif choice == "6":
            view_students()
        elif choice == "7":
            enter_grade()
        elif choice == "0":
            break

# ================= COURSE =================
def add_course():
    cid = input("Course ID: ")
    sem = input("Semester: ")

    for c in courses:
        if c["id"] == cid and c["sem"] == sem:
            print("Duplicate course in the same semester")
            return

    courses.append({
        "id": cid,
        "name": input("Course name: "),
        "credit": input("Credits: "),
        "sem": sem
    })
    print("Course added")

def view_courses():
    for c in courses:
        print(c)

def course_menu():
    while True:
        print("\n===== COURSE MANAGEMENT =====")
        print("1. Add course")
        print("2. View courses")
        print("0. Back")
        choice = input("Choose: ")

        if choice == "1":
            add_course()
        elif choice == "2":
            view_courses()
        elif choice == "0":
            break

# ================= MAIN =================
def main():
    while True:
        print("\n===== STUDENT MANAGEMENT SYSTEM =====")
        print("1. Account management")
        print("2. Student management")
        print("3. Lecturer management")
        print("4. Course management")
        print("0. Exit")
        choice = input("Choose: ")

        if choice == "1":
            account_menu()
        elif choice == "2":
            student_menu()
        elif choice == "3":
            lecturer_menu()
        elif choice == "4":
            course_menu()
        elif choice == "0":
            print("Exit program")
            break

main()
