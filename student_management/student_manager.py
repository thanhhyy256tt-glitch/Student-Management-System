import re
from models import Student, ValidationError, parse_date
from repository import StudentRepository


EMAIL_REGEX = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"


class StudentManager:
    def __init__(self, repo: StudentRepository):
        self.repo = repo

    def add_student(self, student_id, full_name, dob, gender, phone, email, address):
        if not student_id or not full_name:
            raise ValidationError("Student ID and Full name are required")

        if self.repo.get(student_id):
            raise ValidationError("Duplicate student ID")

        if not re.match(EMAIL_REGEX, email):
            raise ValidationError("Invalid email format")

        student = Student(
            student_id=student_id,
            full_name=full_name,
            date_of_birth=parse_date(dob),
            gender=gender,
            phone=phone,
            email=email,
            address=address,
        )
        self.repo.add(student)

    def update_student(self, student_id, **kwargs):
        student = self.repo.get(student_id)
        if not student:
            raise ValidationError("Student not found")

        for key, value in kwargs.items():
            if value:
                setattr(student, key, value)

        self.repo.update(student)

    def delete_student(self, student_id):
        if not self.repo.delete(student_id):
            raise ValidationError("Student not found")

    def list_students(self):
        return self.repo.list_all()
