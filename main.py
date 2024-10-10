def calculate_total_with_percentage(number, percentage):
    # حساب النسبة
    percent_value = (percentage / 100) * number
    # جمع الرقم الأصلي مع النسبة
    total = number + percent_value
    return total

# إدخال الرقم من المستخدم
user_input = float(input("أدخل الرقم: "))
percentage = 14

# حساب الناتج
result = calculate_total_with_percentage(user_input, percentage)

# عرض الناتج
print(f"الناتج هو: {result}")
