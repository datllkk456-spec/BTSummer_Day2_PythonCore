students_score = [
    {"name": "An", "gpa": 7.5},
    {"name": "Bình", "gpa": 6.2},
    {"name": "Cường", "gpa": 4.8},
    {"name": "Dũng", "gpa": 8.0}
]

# Khởi tạo cờ
all_passed = True

# Kiểm tra GPA
for s in students_score:
    if s["gpa"] < 5.0:
        all_passed = False

print("Tất cả sinh viên đều qua môn:", all_passed)