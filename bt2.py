orders = [15000000, 5000000, 22000000, 800000, 12000000]

# Khởi tạo tổng doanh thu và số đơn VIP
total_revenue = 0
vip_count = 0

# Tính tổng doanh thu và đếm đơn VIP
for price in orders:
    total_revenue += price
    if price > 10000000:
        vip_count += 1

print(f"Tổng doanh thu: {total_revenue:,} VNĐ")
print(f"Số đơn VIP: {vip_count} đơn")