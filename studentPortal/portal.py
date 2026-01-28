from pathlib import Path
from storage import Storage

DATA_DIR = Path(__file__).parent / "data"


class StudentPortal:
    def __init__(self):
        self.storage = Storage(DATA_DIR)

    # ========= 1. LOGIN =========
    # accounts.txt format:
    # username|password|role|student_id
    # sv01|123|student|SV01
    def login(self, username: str, password: str):
        rows = self.storage.read_rows("accounts.txt")
        for r in rows:
            if len(r) < 4:
                continue
            u, p, role, student_id = r
            if u == username and p == password and role == "student":
                return student_id
        return None

    # ========= 2. UPDATE PERSONAL INFO =========
    # students.txt: student_id|name|phone|email
    def update_personal_info(self, student_id, name, phone, email):
        rows = self.storage.read_rows("students.txt")
        found = False

        for r in rows:
            if r[0] == student_id:
                r[1], r[2], r[3] = name, phone, email
                found = True

        if not found:
            rows.append([student_id, name, phone, email])

        self.storage.write_rows("students.txt", rows)

    # ========= 3. REGISTER COURSE =========
    # registrations.txt: student_id|course_id
    def register_course(self, student_id, course_id):
        rows = self.storage.read_rows("registrations.txt")
        rows.append([student_id, course_id])
        self.storage.write_rows("registrations.txt", rows)

    # ========= 4. CANCEL COURSE =========
    def cancel_course(self, student_id, course_id):
        rows = self.storage.read_rows("registrations.txt")
        rows = [r for r in rows if not (r[0] == student_id and r[1] == course_id)]
        self.storage.write_rows("registrations.txt", rows)

    # ========= 5. VIEW GRADES =========
    # grades.txt: student_id|course_id|grade
    def view_grades(self, student_id):
        rows = self.storage.read_rows("grades.txt")
        return [r for r in rows if r[0] == student_id]

    # ========= 6. VIEW ASSIGNED COURSES =========
    def view_assigned_courses(self, student_id):
        rows = self.storage.read_rows("registrations.txt")
        return [r[1] for r in rows if r[0] == student_id]
