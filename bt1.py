orders = [
    {"id": "DH01", "name": "iPhone 15 Pro Max", "price": 32000000},
    {"id": "DH02", "name": "Tai nghe AirPods Pro", "price": 5500000},
    {"id": "DH03", "name": "MacBook Pro M3 Max", "price": 65000000},
    {"id": "DH04", "name": "Chuot khong day", "price": 450000},
    {"id": "DH05", "name": "Samsung Galaxy S24", "price": 22000000}
]

total_revenue = 0
vip_count = 0
is_suspicious = False

# Gán đơn đầu tiên làm lớn nhất và nhỏ nhất
max_order = orders[0]
min_order = orders[0]

# Duyệt danh sách
for order in orders:
    # Tính tổng doanh thu
    total_revenue += order["price"]

    # Đếm đơn VIP
    if order["price"] >= 15000000:
        vip_count += 1

    # Tìm đơn lớn nhất
    if order["price"] > max_order["price"]:
        max_order = order

    # Tìm đơn nhỏ nhất
    if order["price"] < min_order["price"]:
        min_order = order

    # Cắm cờ
    if order["price"] > 50000000:
        is_suspicious = True
        suspicious_order = order

print(f"Tong doanh thu: {total_revenue:,} VND")
print(f"So don hang VIP (>= 15tr): {vip_count} don")
print(f"Don hang gia tri CAO NHAT: {max_order['id']} - {max_order['name']} ({max_order['price']:,} VND)")
print(f"Don hang gia tri THAP NHAT: {min_order['id']} - {min_order['name']} ({min_order['price']:,} VND)")

if is_suspicious:
    print(f"CANH BAO RUI RO: Phat hien don {suspicious_order['id']} co gia tri {suspicious_order['price']:,} VND > 50tr!")

print(f"KET LUAN CAM CO: Co is_suspicious = {is_suspicious}")
