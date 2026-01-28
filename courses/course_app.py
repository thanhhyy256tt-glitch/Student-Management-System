# course_app.py

from course_storage import load_courses, save_courses
from course import Course

def add_course(courses):
    course_id = input("Mã môn học: ")
    course_name = input("Tên môn học: ")
    credits = int(input("Số tín chỉ: "))
    semester = input("Học kỳ: ")

    # Không cho trùng môn trong cùng học kỳ
    for c in courses:
        if c.course_id == course_id and c.semester == semester:
            print("❌ Môn học đã tồn tại trong học kỳ này")
            return

    courses.append(Course(course_id, course_name, credits, semester))
    save_courses(courses)
    print("✅ Thêm môn học thành công")


def update_course(courses):
    course_id = input("Nhập mã môn cần sửa: ")
    semester = input("Nhập học kỳ: ")

    for c in courses:
        if c.course_id == course_id and c.semester == semester:
            c.course_name = input("Tên mới: ")
            c.credits = int(input("Số tín chỉ mới: "))
            save_courses(courses)
            print("✅ Cập nhật thành công")
            return

    print("❌ Không tìm thấy môn học")


def delete_course(courses):
    course_id = input("Nhập mã môn cần xóa: ")
    semester = input("Nhập học kỳ: ")

    for c in courses:
        if c.course_id == course_id and c.semester == semester:
            courses.remove(c)
            save_courses(courses)
            print("✅ Đã xóa môn học")
            return

    print("❌ Không tìm thấy môn học")


def view_courses(courses):
    print("\n===== DANH SÁCH MÔN HỌC =====")
    for c in courses:
        print(f"{c.course_id} | {c.course_name} | {c.credits} tín chỉ | HK: {c.semester}")


def main():
    courses = load_courses()

    while True:
        print("\n===== QUẢN LÝ MÔN HỌC =====")
        print("1. Thêm môn học")
        print("2. Sửa môn học")
        print("3. Xóa môn học")
        print("4. Xem danh sách môn học")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            add_course(courses)
        elif choice == "2":
            update_course(courses)
        elif choice == "3":
            delete_course(courses)
        elif choice == "4":
            view_courses(courses)
        elif choice == "0":
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
