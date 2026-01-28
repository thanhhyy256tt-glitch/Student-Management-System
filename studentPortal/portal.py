from __future__ import annotations
from dataclasses import dataclass
from storage import Storage

class AuthError(Exception): ...
class NotFoundError(Exception): ...
class ValidationError(Exception): ...

@dataclass
class StudentPortal:
    storage: Storage

    # UC1: Login
    def login(self, username: str, password: str) -> str:
        rows = self.storage.read_rows("accounts.txt")
        for u, pw, role, student_id in rows:
            if u == username and pw == password and role == "student":
                return student_id
        raise AuthError("Invalid username/password")

    # UC2: Update personal information
    def update_personal_info(self, student_id: str, full_name: str, dob: str,
                             gender: str, phone: str, email: str, address: str) -> None:
        if not full_name.strip():
            raise ValidationError("Full name is required")
        parts = dob.split("/")
        if len(parts) != 3 or not all(p.isdigit() for p in parts):
            raise ValidationError("DOB must be DD/MM/YYYY")
        if "@" not in email:
            raise ValidationError("Invalid email")

        students = self.storage.read_rows("students.txt")
        for i, s in enumerate(students):
            if s[0] == student_id:
                students[i] = [student_id, full_name, dob, gender, phone, email, address]
                self.storage.write_rows("students.txt", students)
                return
        raise NotFoundError("Student not found")

    # UC3: Register for courses
    def register_course(self, student_id: str, course_id: str) -> None:
        courses = self.storage.read_rows("courses.txt")
        if not any(c[0] == course_id for c in courses):
            raise NotFoundError("Course not found")

        regs = self.storage.read_rows("registrations.txt")
        if any(r[0] == student_id and r[1] == course_id for r in regs):
            raise ValidationError("Already registered")
        regs.append([student_id, course_id])
        self.storage.write_rows("registrations.txt", regs)

    # UC4: Cancel course registration
    def cancel_registration(self, student_id: str, course_id: str) -> None:
        regs = self.storage.read_rows("registrations.txt")
        new_regs = [r for r in regs if not (r[0] == student_id and r[1] == course_id)]
        if len(new_regs) == len(regs):
            raise NotFoundError("Registration not found")
        self.storage.write_rows("registrations.txt", new_regs)

    # UC5: View grades
    def view_grades(self, student_id: str) -> list[tuple[str, str]]:
        grades = self.storage.read_rows("grades.txt")
        return [(g[1], g[2]) for g in grades if g[0] == student_id]

    # UC6: View assigned courses
    def view_assigned_courses(self, student_id: str) -> list[str]:
        assigned = self.storage.read_rows("assigned_courses.txt")
        if assigned:
            return [a[1] for a in assigned if a[0] == student_id]
        regs = self.storage.read_rows("registrations.txt")
        return [r[1] for r in regs if r[0] == student_id]

    # Extra: View student list
    def list_students(self) -> list[list[str]]:
        return self.storage.read_rows("students.txt")
