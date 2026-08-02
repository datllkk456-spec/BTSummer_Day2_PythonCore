students = [
    {"id": "SV01", "name": " Nguyen Van An ", "email": " an.nguyen@rikkei.edu.vn ", "phone": " 0987654321 "},
    {"id": "SV02", "name": " Tran Thi Bich ", "email": " bich_gmail.com ", "phone": " 0912345678 "},
    {"id": "SV03", "name": " Le Hoang Cuong ", "email": " cuong@gmail.com ", "phone": " 09876abcde "},
    {"id": "SV04", "name": " Pham Minh Dung ", "email": " dung@gmail.com ", "phone": " 0355667788 "}
]

# Duyệt từng sinh viên
for student in students:
    # Làm sạch dữ liệu
    student["name"] = student["name"].strip()
    student["email"] = student["email"].strip()
    student["phone"] = student["phone"].strip()

    # Kiểm tra email
    email = student["email"]
    valid_email = (
        email.count("@") == 1
        and (email.endswith(".com") or email.endswith(".edu.vn"))
    )

    # Kiểm tra số điện thoại
    phone = student["phone"]
    valid_phone = (
        len(phone) == 10
        and phone.startswith("0")
        and phone.isdigit()
    )

    # In kết quả
    if valid_email and valid_phone:
        print(f"[{student['id']}] {student['name']} | Email: {email} | SDT: {phone} -> HO SO HOP LE")
    elif not valid_email:
        print(f"[{student['id']}] {student['name']} | Email: {email} | SDT: {phone} -> KHONG HOP LE (Thieu @)")
    else:
        print(f"[{student['id']}] {student['name']} | Email: {email} | SDT: {phone} -> KHONG HOP LE (SDT chua chu)")
