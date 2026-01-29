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
        for r in rows:
            if len(r) >= 2 and r[0] == student_id and r[1] == course_id:
               return False
        rows.append([student_id, course_id])
        self.storage.write_rows("registrations.txt", rows)
        return True

    # ========= 4. CANCEL COURSE =========
    def cancel_course(self, student_id, course_id):
        rows = self.storage.read_rows("registrations.txt")
        new_rows = [r for r in rows if not (len(r) >= 2 and r[0] == student_id and r[1] == course_id)]
        if len(new_rows) == len(rows):
           return False
        self.storage.write_rows("registrations.txt", new_rows)
        return True

    # ========= 5. VIEW GRADES =========
    # grades.txt: student_id|course_id|grade
    def view_grades(self, student_id):
        rows = self.storage.read_rows("grades.txt")
        return [r for r in rows if r[0] == student_id]

    # ========= 6. VIEW ASSIGNED COURSES =========
    # assigned_courses.txt: student_id|course_id
    def view_assigned_courses(self, student_id):
        rows = self.storage.read_rows("assigned_courses.txt")
        return [r[1] for r in rows if len(r) >= 2 and r[0] == student_id]
        
    # ========= 7. VIEW STUDENT LIST =========
    # students.txt: student_id|name|phone|email
    def view_student_list(self):
        rows = self.storage.read_rows("students.txt")
        # trả về list dict cho dễ in
        return [
            {"student_id": r[0], "name": r[1], "phone": r[2], "email": r[3]}
            for r in rows
            if len(r) >= 4
        ]
