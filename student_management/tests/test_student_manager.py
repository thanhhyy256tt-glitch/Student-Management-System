import unittest
import os
from repository import StudentRepository
from student_manager import StudentManager
from models import ValidationError


class TestStudentManager(unittest.TestCase):
    def setUp(self):
        self.file = "test_students.json"
        if os.path.exists(self.file):
            os.remove(self.file)
        self.repo = StudentRepository(self.file)
        self.manager = StudentManager(self.repo)

    def tearDown(self):
        if os.path.exists(self.file):
            os.remove(self.file)

    def test_add_student(self):
        self.manager.add_student(
            "SV01", "Nguyen Van A", "01/01/2006",
            "Nam", "0901234567", "a@gmail.com", "HCM"
        )
        self.assertEqual(len(self.manager.list_students()), 1)

    def test_duplicate_id(self):
        self.manager.add_student(
            "SV01", "A", "01/01/2006",
            "Nam", "0901", "a@gmail.com", "HCM"
        )
        with self.assertRaises(ValidationError):
            self.manager.add_student(
                "SV01", "B", "01/01/2006",
                "Nam", "0902", "b@gmail.com", "HCM"
            )


if __name__ == "__main__":
    unittest.main()
