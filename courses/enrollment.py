# enrollment.py

import os

FILE_NAME = os.path.join(os.path.dirname(__file__), "enrollments.txt")

def enroll(student_id, course_id, semester):
    record = f"{student_id},{course_id},{semester}\n"

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip() == record.strip():
                    print("❌ Sinh viên đã đăng ký môn này")
                    return

    with open(FILE_NAME, "a", encoding="utf-8") as f:
        f.write(record)

    print("✅ Đăng ký môn học thành công")


def view_enrollments():
    print("\n===== DANH SÁCH ĐĂNG KÝ =====")
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            student_id, course_id, semester = line.strip().split(",")
            print(f"Sinh viên: {student_id} | Môn: {course_id} | HK: {semester}")
