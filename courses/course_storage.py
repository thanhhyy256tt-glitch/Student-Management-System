# course_storage.py

import os
from course import Course

FILE_NAME = os.path.join(os.path.dirname(__file__), "courses.txt")

def load_courses():
    courses = []
    if not os.path.exists(FILE_NAME):
        return courses

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            course = Course.from_string(line)
            if course:
                courses.append(course)
    return courses


def save_courses(courses):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for c in courses:
            f.write(c.to_string())
