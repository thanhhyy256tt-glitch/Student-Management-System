import json
from pathlib import Path
from typing import Dict, List, Optional
from models import Student


class StudentRepository:
    def __init__(self, filename: str = "students.json"):
        self.path = Path(filename)
        self.students: Dict[str, Student] = {}
        self.load()

    def load(self):
        if not self.path.exists():
            return
        data = json.loads(self.path.read_text(encoding="utf-8"))
        for sid, s in data.items():
            self.students[sid] = Student.from_dict(s)

    def save(self):
        data = {sid: s.to_dict() for sid, s in self.students.items()}
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def add(self, student: Student):
        self.students[student.student_id] = student
        self.save()

    def update(self, student: Student):
        self.students[student.student_id] = student
        self.save()

    def delete(self, student_id: str) -> bool:
        if student_id not in self.students:
            return False
        del self.students[student_id]
        self.save()
        return True

    def get(self, student_id: str) -> Optional[Student]:
        return self.students.get(student_id)

    def list_all(self) -> List[Student]:
        return list(self.students.values())
