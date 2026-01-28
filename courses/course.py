# course.py

class Course:
    def __init__(self, course_id, course_name, credits, semester):
        self.course_id = course_id
        self.course_name = course_name
        self.credits = credits
        self.semester = semester

    def to_string(self):
        return f"{self.course_id},{self.course_name},{self.credits},{self.semester}\n"

    @staticmethod
    def from_string(line):
        parts = line.strip().split(",")
        if len(parts) == 4:
            return Course(parts[0], parts[1], int(parts[2]), parts[3])
        return None
