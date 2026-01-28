# app.py

from storage import load_accounts, save_accounts
from account import Account

current_user = None

def create_account(accounts):
    username = input("Username: ")
    password = input("Password: ")
    role = input("Role (admin/student/teacher): ")

    for acc in accounts:
        if acc.username == username:
            print("❌ Tài khoản đã tồn tại")
            return

    accounts.append(Account(username, password, role))
    save_accounts(accounts)
    print("✅ Tạo tài khoản thành công")


def login(accounts):
    global current_user

    print("\n===== ĐĂNG NHẬP =====")
    username = input("Username: ")
    password = input("Password: ")

    for acc in accounts:
        if acc.username == username and acc.password == password:
            current_user = acc
            print(f"✅ Đăng nhập thành công ({acc.role})")
            return

    print("❌ Sai username hoặc password")


def logout():
    global current_user
    current_user = None
    print("✅ Đã đăng xuất")


def check_role():
    if current_user:
        print(f"🔐 Quyền: {current_user.role}")
    else:
        print("❌ Chưa đăng nhập")


def show_accounts(accounts):
    if not current_user or current_user.role != "admin":
        print("❌ Chỉ ADMIN mới được xem danh sách")
        return

    print("\n===== DANH SÁCH TÀI KHOẢN =====")
    for acc in accounts:
        print(f"{acc.username} | {acc.role}")


def delete_account(accounts):
    if not current_user or current_user.role != "admin":
        print("❌ Chỉ ADMIN mới được xóa tài khoản")
        return

    username = input("Nhập username cần xóa: ")

    for acc in accounts:
        if acc.username == username:
            accounts.remove(acc)
            save_accounts(accounts)
            print("✅ Đã xóa tài khoản")
            return

    print("❌ Không tìm thấy tài khoản")


def main():
    accounts = load_accounts()

    while True:
        print("\n===== QUẢN LÝ TÀI KHOẢN =====")
        print("1. Tạo tài khoản")
        print("2. Đăng nhập")
        print("3. Đăng xuất")
        print("4. Kiểm tra phân quyền")
        print("5. Xem danh sách tài khoản")
        print("6. Xóa tài khoản")
        print("0. Thoát")

        choice = input("Chọn: ")

        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            login(accounts)
        elif choice == "3":
            logout()
        elif choice == "4":
            check_role()
        elif choice == "5":
            show_accounts(accounts)
        elif choice == "6":
            delete_account(accounts)
        elif choice == "0":
            print("👋 Thoát chương trình")
            break
        else:
            print("❌ Lựa chọn không hợp lệ")


if __name__ == "__main__":
    main()
