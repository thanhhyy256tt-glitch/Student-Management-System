from storage import load_data, save_data

current_lecturer = None

# ===== QUẢN LÝ GIẢNG VIÊN =====
def add_lecturer():
    data = load_data("lecturers.txt")
    lid = input("Mã GV: ")
    name = input("Tên GV: ")
    password = input("Mật khẩu: ")

    data.append([lid, name, password])
    save_data("lecturers.txt", data)
    print("✅ Thêm giảng viên thành công")

def delete_lecturer():
    data = load_data("lecturers.txt")
    lid = input("Nhập mã GV cần xóa: ")

    data = [l for l in data if l[0] != lid]
    save_data("lecturers.txt", data)
    print("✅ Đã xóa giảng viên")

def update_lecturer():
    data = load_data("lecturers.txt")
    lid = input("Mã GV cần cập nhật: ")

    for l in data:
        if l[0] == lid:
            l[1] = input("Tên mới: ")
            l[2] = input("Mật khẩu mới: ")

    save_data("lecturers.txt", data)
    print("✅ Cập nhật thành công")

def assign_course():
    assigns = load_data("assignments.txt")
    lid = input("Mã GV: ")
    cid = input("Mã môn học: ")

    assigns.append([lid, cid])
    save_data("assignments.txt", assigns)
    print("✅ Phân công môn học thành công")

# ===== GIẢNG VIÊN =====
def lecturer_login():
    global current_lecturer
    lecturers = load_data("lecturers.txt")

    lid = input("Mã GV: ")
    password = input("Mật khẩu: ")

    for l in lecturers:
        if l[0] == lid and l[2] == password:
            current_lecturer = l
            print("✅ Đăng nhập thành công")
            return
    print("❌ Sai thông tin đăng nhập")

def view_my_courses():
    assigns = load_data("assignments.txt")
    courses = load_data("courses.txt")

    print("\n===== MÔN HỌC ĐƯỢC PHÂN CÔNG =====")
    for a in assigns:
        if a[0] == current_lecturer[0]:
            for c in courses:
                if c[0] == a[1]:
                    print(f"- {c[1]}")

def view_students():
    students = load_data("students.txt")
    print("\n===== DANH SÁCH SINH VIÊN =====")
    for s in students:
        print(f"{s[0]} - {s[1]}")

def enter_grade():
    grades = load_data("grades.txt")
    sid = input("Mã SV: ")
    cid = input("Mã môn: ")
    score = input("Điểm: ")

    grades.append([sid, cid, score])
    save_data("grades.txt", grades)
    print("✅ Nhập điểm thành công")

# ===== MENU =====
def main():
    while True:
        print("""
===== QUẢN LÝ GIẢNG VIÊN =====
1. Thêm giảng viên
2. Xóa giảng viên
3. Cập nhật giảng viên
4. Phân công môn học
5. Giảng viên đăng nhập
6. Xem môn được phân công
7. Xem danh sách sinh viên
8. Nhập điểm
0. Thoát
""")
        c = input("Chọn: ")

        if c == "1": add_lecturer()
        elif c == "2": delete_lecturer()
        elif c == "3": update_lecturer()
        elif c == "4": assign_course()
        elif c == "5": lecturer_login()
        elif c == "6": view_my_courses()
        elif c == "7": view_students()
        elif c == "8": enter_grade()
        elif c == "0": break

if __name__ == "__main__":
    main()
